import pandas as pd
import matplotlib.pyplot as plt

# Skiping row 1 and 2 since they only contain coordinates of countries
df_confirmed = pd.read_csv('data/time_series_covid19_confirmed_global.csv', index_col=0, skiprows=[1,2])
df_search = pd.read_csv('data/time_serie_coronavirus_searches.csv', index_col=0)
print(df_search)


df_confirmed_country = pd.DataFrame(df_confirmed, columns=['Austria'])
df_search_country = pd.DataFrame(df_search, columns=['Austria'])
df = df_confirmed_country.merge(df_search_country, left_index=True, right_index=True)
# plt.figure()

# https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html
df['Austria_y'] = df['Austria_y'].astype(str).astype(int)

y = df.plot(secondary_y=['Austria_y'])
y.set_ylabel('Infected')
y.right_ax.set_ylabel('Search amount')
plt.show()