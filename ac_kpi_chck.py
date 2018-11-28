#Import relevant python libraries
import pandas as pd

"""Compare the emails that ordered vis a vis the emails that were sent ActiveCampaign blasts"""

#Read csv of 2 comparative files and store them as dataframes
google=pd.read_csv('KPI_zapped.csv')
google = google.sort_values(by='EMAIL')
print(list(google)) #Official KPI Sheet source
df2=google[['EMAIL']]


acmonth=pd.read_csv('apr2018.csv')
acmonth = acmonth.sort_values(by='EMAIL')
print(list(acmonth))
df1=acmonth[['EMAIL']]

#Note: df2 is a subset of df1


print(df1.head())
print(df2.head())


df_all = df1.merge(df2.drop_duplicates(), on=['EMAIL','EMAIL'], how='left', indicator=True)

df_missing = df_all[df_all['_merge'] == 'left_only']

df_missing.to_csv('missingvalues.csv', sep=',')

df_KPIencode = pd.merge(df_missing,acmonth, on=['EMAIL','EMAIL'])

df_KPIencode.to_csv('encodeonKPI.csv', sep=',')


