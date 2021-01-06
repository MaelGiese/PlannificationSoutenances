import pandas as pd


def load_excel(path):
    df = pd.read_excel(path)
    df = clean_data(df)

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
    df["<DATE TIME>"] = df['<DATE>'] + ' ' + df['<TIME>']
    date_time = pd.to_datetime(df.pop('<DATE TIME>'), format='%Y.%m.%d %H:%M:%S')
    df.drop(['<DATE>', '<TIME>'], axis=1)

    return df


if __name__ == "__main__":
    path = 'Soutenances M1 janvier 2020 - V2.xlsx'
    df = load_excel(path)

    pd.set_option('display.max_columns', None)
    print(df)
