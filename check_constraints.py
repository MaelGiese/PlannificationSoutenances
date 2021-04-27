from data_processing import load_excel
import numpy as np
import pandas as pd


# - si plusieurs étudiants ont le même tuteur entreprise, il est préférable que les soutenances soient groupées.
# - il est préférable que les soutenances d'une même tuteur académique soit groupées.
# Create two list 'tuteurs' and 'tuteurs_soutenances' wich represent the order of passage and their number
def check_tuteur_constraints(df, tuteur_column):
    tuteurs = []
    tuteurs_soutenances = []

    # Value of the first element of the column
    tuteurs.append(df.iloc[0][tuteur_column])
    tuteurs_soutenances.append(0)

    index = 0
    for _, row in df.iterrows():
        if row[tuteur_column] == tuteurs[index]:
            tuteurs_soutenances[index] += 1
        else:
            tuteurs.append(row[tuteur_column])
            tuteurs_soutenances.append(1)

            index += 1

    # A list that contain the indexes of the group of soutenance in the dataset
    soutenances_index = []
    cpt = 0
    for i in tuteurs_soutenances:
        soutenances_index.append(i + cpt)
        cpt += i

    return tuteurs, tuteurs_soutenances, soutenances_index


# Return the tuteurs that have soutenance not grouped and the indexes and the number of not grouped soutenance
def get_tuteur_not_grouped(df, tuteur_columns, treshold):
    if len(tuteur_columns) == 1:
        tuteurs, nb_soutenances, soutenances_index = check_tuteur_constraints(df, tuteur_columns[0])

        not_grouped_tuteurs = []
        not_grouped_soutenances = []
        not_grouped_index = []

        for i in range(len(tuteurs)):
            if nb_soutenances[i] <= treshold:
                not_grouped_tuteurs.append(tuteurs[i])
                not_grouped_soutenances.append(nb_soutenances[i])
                not_grouped_index.append([soutenances_index[i] - nb_soutenances[i], soutenances_index[i] - 1])

        return not_grouped_tuteurs, not_grouped_soutenances, not_grouped_index
    elif len(tuteur_columns) == 2:

        all_tuteurs = np.unique(df[tuteur_columns].values)

        not_grouped_tuteurs = []
        not_grouped_soutenances = []
        not_grouped_index = []

        for t in all_tuteurs:
            cpt = 0
            for i, row in df.iterrows():
                if row[tuteur_columns[0]] == t or row[tuteur_columns[1]] == t:
                    cpt += 1
                else:
                    if 0 < cpt < treshold:
                        not_grouped_tuteurs.append(t)
                        not_grouped_soutenances.append(cpt)
                        not_grouped_index.append([i - cpt, i])
                    cpt = 0

        return not_grouped_tuteurs, not_grouped_soutenances, not_grouped_index
    else:
        print('Too many columns')
        return None


# - chaque enseignant fait a peu près autant de soutenances en tant que président qu'en tant que tuteur
def president_tuteur_diff(df, tuteur_columns):
    column = df[tuteur_columns[0]].value_counts()
    column_1 = df[tuteur_columns[1]].value_counts()
    diff = column - column_1
    diff = diff.replace(0, np.nan).dropna(axis=0)

    return diff


# - un tuteur ne peut pas etre a deux endroits a la fois
def check_tuteur_unique_time(df, tuteur_columns, room_column, start_hour_column):
    times = df[start_hour_column].unique()

    duplicates_tuteurs = []
    duplicates_times = []
    duplicates_room = []

    # Pour chaque horaire de soutenance on regarde si un tuteur n'apparait pas deux fois
    for t in times:
        times_duplicates = df.loc[(df[start_hour_column] == t)]
        tuteurs_in_t = times_duplicates[[tuteur_columns[0], tuteur_columns[1]]].values.ravel()
        u, c = np.unique(tuteurs_in_t, return_counts=True)
        duplicates = u[c > 1]

        if len(duplicates) > 0:
            tuteurs = []
            times = []
            rooms = []
            for d in duplicates:
                tuteurs.append(d)
                times.append(t)
                room = []
                for r in times_duplicates[room_column]:
                    room.append(r)
                rooms.append(room)

            duplicates_tuteurs.append(tuteurs)
            duplicates_times.append(times)
            duplicates_room.append(rooms)

    return duplicates_tuteurs, duplicates_times, duplicates_room


if __name__ == "__main__":
    # path = 'Documents/Soutenances M1 janvier 2020.xlsx'
    path = 'Documents/Soutenances M1 janvier 2020 - Contraintes.xlsx'
    df = load_excel(path)

    tuteur_columns = ['Président', 'Tuteur Université']
    start_hour_column = 'Heure Début'
    end_hour_column = 'Heure Fin'
    date_column = 'Date'
    room_column = 'Salle'

    treshold = 2
    not_grouped_tuteurs, soutenances, index = get_tuteur_not_grouped(df, tuteur_columns, treshold)

    # Affiche les contraintes non respectées dans la console
    print('#################################################')
    print('TUTEUR AYANT DES SOUTENANCES NON GROUPEES')
    if len(not_grouped_tuteurs) == 0:
        print('Aucun tuteur trouvé')
    for i in range(len(not_grouped_tuteurs)):
        print(not_grouped_tuteurs[i] + ' a ' + str(soutenances[i]) +
              ' soutenances non groupée, de ' +
              str(df.iloc[index[i][0]][start_hour_column].hour) + 'h' +
              str(df.iloc[index[i][0]][start_hour_column].minute) +
              ' a ' +
              str(df.iloc[index[i][1]][end_hour_column].hour) + 'h' +
              str(df.iloc[index[i][1]][end_hour_column].minute) +
              ', ' +
              str(df.iloc[index[i][1]][date_column]))

    print('\n#################################################')
    print('DIFFERENCE NOMBRE DE SEANCES PRESIDENT/TUTEUR')
    diff = president_tuteur_diff(df, tuteur_columns)
    print(diff)

    print('\n#################################################')
    print('UN TUTEUR NE PEUT PAS ETRE A DEUX ENDROIT A LA FOIS')
    duplicates_tuteurs, duplicates_times, duplicates_room = check_tuteur_unique_time(df, tuteur_columns, room_column, start_hour_column)
    if len(duplicates_tuteurs) == 0:
        print('Aucun tuteur n\'est a deux endroits a la fois')
    for i in range(len(duplicates_tuteurs)):
        for j in range(len(duplicates_tuteurs[i])):
            print()
            print(duplicates_tuteurs[i][j] + ' est présent a plusieurs soutenance a l\'horaire : ' +
                  np.datetime_as_string(duplicates_times[i][j], unit='m'))
            print('dans les salles : ')
            for s in duplicates_room[i][j]:
                print('- ' + str(s))
