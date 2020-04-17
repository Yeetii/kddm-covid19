import pandas as pd
import matplotlib.pyplot as plt

# https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html

def plot_country(df_cases, df_search):
    df = df_cases.merge(df_search, left_index=True, right_index=True)

    # Plot search dataframe on right axis and cases on left axis
    cases_col_name = df.columns.values[0]
    search_col_name = df.columns.values[1]

    y = df.plot(secondary_y=[search_col_name])
    y.set_ylabel('Amount of people')
    y.right_ax.set_ylabel('Search amount')
    # Shows plot in window
    # plt.show()
    # Saves plot as a png
    plt.savefig(search_col_name + "|" + cases_col_name)
    # Without this plot remains in memory
    plt.close()

def add_suffix_first_col(df, suffix):
    name = df.columns.values[0]
    df = df.rename(columns={name: name + suffix})
    return df

def plot_all_countries(df_cases, df_search):
    for col in df_cases.columns:
        df_confirmed_country = pd.DataFrame(df_cases, columns=[col])
        df_search_country = pd.DataFrame(df_search, columns=[col])
        df_confirmed_country = add_suffix_first_col(df_confirmed_country, "_Confirmed")
        df_search_country = add_suffix_first_col(df_search_country, "_Search-Coronavirus")
        plot_country(df_confirmed_country, df_search_country)

# Skiping row 1 and 2 since they only contain coordinates of countries
df_confirmed = pd.read_csv('data/time_series_covid19_confirmed_global.csv', index_col=0, skiprows=[1,2])
df_search = pd.read_csv('data/time_serie_coronavirus_searches.csv', index_col=0)
plot_all_countries(df_confirmed, df_search)