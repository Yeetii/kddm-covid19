import pandas as pd
import matplotlib.pyplot as plt

# https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html

def plot_country_internal(df):
    # Plot search dataframe on right axis and cases on left axis
    search_col_name = df.columns.values[1]
    y = df.plot(secondary_y=[search_col_name])
    y.set_ylabel('Amount of people')
    y.right_ax.set_ylabel('Search amount')

def plot_country_window(df):
    plot_country_internal(df)
    # Shows plot in window
    plt.show()
    # # Without this plot remains in memory
    plt.close()

def plot_country_save(df):
    cases_col_name = df.columns.values[0]
    search_col_name = df.columns.values[1]
    plot_country_internal(df)
    # Saves plot as a png
    plt.savefig(search_col_name + "|" + cases_col_name)
    # Without this plot remains in memory
    plt.close()



def add_suffix_first_col(df, suffix):
    name = df.columns.values[0]
    df = df.rename(columns={name: name[:-2] + suffix})
    return df

def merge_dataframes(df_cases, df_search):
    dfs_merged = []
    for col in df_cases.columns:
        df_cases_country = pd.DataFrame(df_cases, columns=[col])
        df_search_country = pd.DataFrame(df_search, columns=[col])
        df = df_cases_country.merge(df_search_country, left_index=True, right_index=True)
        dfs_merged.append(df)
    return dfs_merged

def rename_columns(df, first_suffix, second_suffix):
    first_name = df.columns.values[0]
    second_name = df.columns.values[1]
    df = df.rename(columns={first_name: first_name[:-2] + first_suffix, second_name: second_name[:-2] + second_suffix})
    return df

# Skiping row 1 and 2 since they only contain coordinates of countries
df_confirmed = pd.read_csv('data/time_series_covid19_confirmed_global.csv', index_col=0, skiprows=[1,2])
df_search = pd.read_csv('data/time_serie_coronavirus_searches.csv', index_col=0)
dfs = merge_dataframes(df_confirmed, df_search)
dfs = map(lambda df : rename_columns(df, "_Confirmed", "_Search-Coronavirus"), dfs)
for df in dfs:
    plot_country_save(df)