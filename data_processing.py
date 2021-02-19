import pandas as pd


def load_excel(path):
    df = pd.read_excel(path)
    df = clean_data(df)
    df = create_datetime(df)

    return df


def clean_data(df):
    # Drop the columns containing only NaN
    df = df.dropna(axis=1, how='all')
    # Drop the rows containing only NaN
    df = df.dropna(axis=0, how='all')
    # Drop columns containing one or more NaN
    df = df.dropna(axis='columns')

    return df

# Need an other Date/Heure format
def create_datetime(df):
    df['Heure Début'] = df['Heure Début'].astype(str)
    df['Heure Fin'] = df['Heure Début'].astype(str)

    df['Heure Début'] = df['Date'] + ' ' + df['Heure Début']
    df['Heure Fin'] = df['Date'] + ' ' + df['Heure Fin']

    df['Heure Début'] = pd.to_datetime(df.pop('Heure Début'), format='%Y.%m.%d %H:%M:%S')
    df['Heure Fin'] = pd.to_datetime(df.pop('Heure Fin'), format='%Y.%m.%d %H:%M:%S')
    df['Date'] = pd.to_datetime(df.pop('Date'), format='%Y.%m.%d')

    # df.drop(['date'], axis=1)

    return df


if __name__ == "__main__":
    path = 'Soutenances M1 janvier 2020 - Contraintes.xlsx'
    df = load_excel(path)

    pd.set_option('display.max_columns', None)
    print(df)
