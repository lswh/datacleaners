#Import relevant python libraries
import pandas as pd


# Get old 1 million rows of data
old=pd.read_csv('Old1M.csv')
old=old.sort_values(by='RANK')
print(list(old))
print(old.head())


# Get top 25k data
twofive=pd.read_csv('25kclean430.csv')
twofive=twofive.sort_values(by='RANK')
print(twofive.head())


#Split old data to match fields of 25k data
old['SITE'],old['EXT1']=old['SITE'].str.split('.', 1).str

print(old.head())

old['EXT1'],old['EXT2']=old['EXT1'].str.split('.', 1).str

print(old.head())

#Subset old data and remove rank 1 to 25,000
cleanold = old.loc[old['RANK'] >= 25001]

print(cleanold.head())

#Reorder the columns to match the 25k dataset standard
cleanold = cleanold[['SITE','EXT1','EXT2','COMPLIANCE','RANK']]
print(cleanold.head())
print(twofive.head())

#Combine everything
joinforces = [twofive,cleanold]
result1 = pd.concat(joinforces)
print(result1.head())
print(result1.tail())


additional = pd.read_csv('additional.csv')
addiranks = pd.read_csv('125to400.csv')
print(addiranks.head())
print(additional.head())

addthis =pd.merge(addiranks,additional,on='SITE', how='outer')
addthis =  addthis[['SITE','EXT1','EXT2','COMPLIANCE','RANK']]
print(addthis.head())
print(addthis.tail())

#Concatenate additional rows to the other combined dataset result1
joinforces2 = [result1,addthis]
resulta = pd.concat(joinforces2)
resulta = resulta.sort_values(by='RANK')

resulta.to_csv("1Mcombined_raw.csv", encoding='utf-8', index=False)


#Rank 1 m plus no blanks
resulta2=pd.read_csv('1Mplus_NoBlanks.csv', encoding='utf-8')
resulta2=resulta2.sort_values(by='RANK')
resulta2.to_csv("1MPlus_NoBlanks_Sorted.csv", encoding='utf-8')