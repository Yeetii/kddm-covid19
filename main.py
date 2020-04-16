import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/time_series_covid19_confirmed_global.csv')
df = df.drop([0,1])
print(df)

   
df = pd.DataFrame(df,columns=['Austria','Country/Region'])
df.plot(x ='Country/Region', y='Austria', kind = 'scatter')
plt.show()