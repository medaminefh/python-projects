import pandas as pd

fdf = pd.read_csv(r'Data\Stats\federer_stats.csv')
ndf = pd.read_csv(r'Data\Stats\nadal_stats.csv')
ddf = pd.read_csv(r'Data\Stats\djokovic_stats.csv')

ddf = ddf.replace("-",0)
fdf = fdf.replace("-",0)
ndf = ndf.replace("-",0)

dflist = [fdf, ndf, ddf]

def data_cleaning(df):

    df['Total wins'] = df['Summary'].str.split("/").str[0]
    df['Total loss'] = df['Summary'].str.split("/").str[1]
    df['Clay wins'] = df['Clay'].str.split("/").str[0]
    df['Clay loss'] = df['Clay'].str.split("/").str[1]
    df['Hard wins'] = df['Hard'].str.split("/").str[0]
    df['Hard loss'] = df['Hard'].str.split("/").str[1]
    df['Indoor wins'] = df['Indoor'].str.split("/").str[0]
    df['Indoor loss'] = df['Indoor'].str.split("/").str[1]
    df['Grass wins'] = df['Grass'].str.split("/").str[0]
    df['Grass loss'] = df['Grass'].str.split("/").str[1]
    df.drop(columns=["Summary","Clay","Hard","Indoor","Grass","Not Set"], inplace=True)
    df.fillna(0, inplace=True)
    df = df.apply(pd.to_numeric)
    df['Hard wins'] = df['Hard wins'] + df['Indoor wins']
    df['Hard loss'] = df['Hard loss'] + df['Indoor loss']
    df.drop(columns=["Indoor wins","Indoor loss"], inplace=True)
    df.set_index("Year", inplace=True)
    df['Total wins %'] = df['Total wins'] / (df['Total wins'] + df['Total loss'])
    df['Total wins %'] = df['Total wins %'].round(decimals=4) * 100
    df['Clay wins %'] = df['Clay wins'] / (df['Clay wins'] + df['Clay loss'])
    df['Clay wins %'] = df['Clay wins %'].round(decimals=4) * 100
    df['Hard wins %'] = df['Hard wins'] / (df['Hard wins'] + df['Hard loss'])
    df['Hard wins %'] = df['Hard wins %'].round(decimals=4) * 100
    df['Grass wins %'] = df['Grass wins'] / (df['Grass wins'] + df['Grass loss'])
    df['Grass wins %'] = df['Grass wins %'].round(decimals=4) * 100

    df.fillna(0, inplace=True)

    return df

new_list = []

for df in dflist:
    new_df = data_cleaning(df)
    new_list.append(new_df)

fdf = new_list[0]
ndf = new_list[1]
ddf = new_list[2]

fdf.drop([1998], axis=0, inplace=True)
ndf.drop([2001], axis=0, inplace=True)
ddf.drop([2003], axis=0, inplace=True)

fdf.to_csv(r'Cleaned Data\federer_stats_cleaned.csv')
ndf.to_csv(r'Cleaned Data\nadal_stats_cleaned.csv')
ddf.to_csv(r'Cleaned Data\djokovic_stats_cleaned.csv')
