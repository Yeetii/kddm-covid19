import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/time_series_covid19_confirmed_global.csv', index_col=0)
df = df.drop(['Lat', 'Long'])
print(df)

   
# df = pd.DataFrame(df,columns=['Australia','Austria'])
# df.plot(x ='Country/Region', y='Austria', kind = 'scatter')
# plt.show()

df = pd.DataFrame(df, columns=['Austria', 'Sweden'])
df.plot(subplots=True)
# plt.legend()
plt.show()