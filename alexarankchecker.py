#Import relevant python libraries
import pandas as pd

"""Compare the emails that ordered vis a vis the emails that were sent ActiveCampaign blasts"""

#Read csv of 2 comparative files and store them as dataframes
alexa=pd.read_csv('25k.csv')
print(list(alexa)) #Rank and Site

scraped=pd.read_csv('25kscrapy.csv')
print(list(scraped)) #Site, Compliance 

#Initialize empty dataframe as container of matches
matches_list=[]
	
print(alexa.head())
print(scraped.head())


#Merge using a common column. <3 
ermerged = pd.merge(scraped,alexa,on='SITE', how='outer')

print(ermerged.head())

ermerged.to_csv("25k_04212018.csv", encoding='utf-8', index=False) #outer dataset is more complete merged dataset with 1 million rows
