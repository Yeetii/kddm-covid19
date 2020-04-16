import pandas as pd
import matplotlib.pyplot as plt

# Skiping row 1 and 2 since they only contain coordinates of countries
df = pd.read_csv('data/time_series_covid19_confirmed_global.csv', index_col=0, skiprows=[1,2])
print(df)


df = pd.DataFrame(df, columns=['Denmark','Austria', 'Sweden'])
print(df)
df.plot()
plt.show()