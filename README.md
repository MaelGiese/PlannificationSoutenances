# Détection de contraintes
## Dépendances
- numpy
- pandas

## Installation
### Installer les dépendances nécessaire
Le programme nécéssite que python soit installer au préalable sur la machine.
Avant d'installer le programme il faut installer les dépendances, entrer le commande suivante dans la console:
<br />`pip install pandas`
<br />`pip install numpy`
### Installer le programme
Il suffit de télécharger le programme depuis ce dépôt GitHub, ouvrir l'invite de commande dans la racine du projet puis entrer la commande `python check_contraints.py` pour lancer la détection de contraintes sur le fichier `Soutenances M1 janvier 2020 - Contraintes.xlsx`.

## Run
Lancer le fichier `check_contraints.py` pour afficher les contraintes qui ne sont pas respectées
<br /> Le fichier `data_processing.py` traite et formate les données avant de lancer les algorithmes de détection

## Documents
`Soutenances M1 janvier 2020 - Contraintes.xlsx`: Planning avec des violations de contraintes ajoutées manuellement
<br />`Soutenances M1 janvier 2020.xlsx`: Planning avec les violations de contraintes corrigées en fonction des résultats du programme

## Affichage des violations de contraintes
Résultat pour le fichier `Soutenances M1 janvier 2020 - Contraintes.xlsx` avec des voilations de contraintes ajoutées
```
#################################################
TUTEUR AYANT DES SOUTENANCES NON GROUPEES
Anne-Marie Lesas a 1 soutenances non groupée, de 9h0 a 9h30, 2020-01-07 00:00:00
Fabrice Huet a 1 soutenances non groupée, de 8h30 a 9h0, 2020-01-06 00:00:00
Fabrice Huet a 1 soutenances non groupée, de 9h30 a 10h30, 2020-01-06 00:00:00
Michel Buffa a 1 soutenances non groupée, de 8h30 a 9h0, 2020-01-07 00:00:00
Michel Winter a 1 soutenances non groupée, de 9h0 a 9h30, 2020-01-06 00:00:00
Pierre Crescenzo a 1 soutenances non groupée, de 8h30 a 9h0, 2020-01-06 00:00:00

#################################################
DIFFERENCE NOMBRE DE SEANCES PRESIDENT/TUTEUR
Anne-Marie Lesas   -5.0
Fabrice Huet        1.0
Gabriel Mopolo      1.0
Michel Buffa        4.0
Michel Winter      -2.0
Pierre Crescenzo    1.0
dtype: float64

#################################################
UN TUTEUR NE PEUT PAS ETRE A DEUX ENDROIT A LA FOIS

Michel Winter est présent a plusieurs soutenance a l'horaire : 2020-01-06T09:00
dans les salles : 
- Salle du Conseil
- TD 14
```

Résultat pour le fichier `Soutenances M1 janvier 2020.xlsx` avec les violations de contraintes corrigées grace au programme
```
#################################################
TUTEUR AYANT DES SOUTENANCES NON GROUPEES
Aucun tuteur trouvé

#################################################
DIFFERENCE NOMBRE DE SEANCES PRESIDENT/TUTEUR
Anne-Marie Lesas   -4.0
Gabriel Mopolo      1.0
Michel Buffa        3.0
dtype: float64

#################################################
UN TUTEUR NE PEUT PAS ETRE A DEUX ENDROIT A LA FOIS
Aucun tuteur n'est a deux endroits a la fois
```

# Fichier d'entrée
## Format du fichier d'entrée excel

| Colonne                              | Data type |
|:-------------------------------------|:----------|
| Nom du candidat                      | String    |
| Prénom du candidat                   | String    |
| Email du candidat                    | String    |
| Entreprise du candidat               | String    |
| Date                                 | YYYY.MM.DD|
| Heure de début de soutenance         | HH:mm     |
| Heure de fin de soutenance           | HH:mm     |
| Numéro du jury                       | Integer   |
| Salle                                | String    |
| Nom/Prénom du président du jury      | String    |
| Nom/Prénom du tuteur Universitaire   | String    |


## Information manquante nécéssaire a la génération d'un planing (non implémenté)
- Nom prénom du tuteur de l'entreprise
- Plage horaire disponible
- Durées des soutenances
- Les disponibilités/indisponibilités des tuteurs (entreprise et académique)
- Les salles disponibles (nombre et noms des salles)
