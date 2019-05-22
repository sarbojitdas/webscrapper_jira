from bs4 import BeautifulSoup 
import requests
import csv
import pandas as pd
from datetime import datetime
#get the url of the respective website
page=requests.get('https://issues.apache.org/jira/browse/CAMEL-10597')
#parseing the html
soup=BeautifulSoup(page.content,'html.parser')
# find div tag and class for the respective fields
items=soup.find_all(class_="aui-group issue-body")

bug=items[0].find(class_='value').get_text()
assign=items[0].find(class_='user-hover').get_text()
descrip=items[0].find('p').get_text()
date=items[0].find(class_='livestamp').get_text()
#create a list
report=[]
#store all the fields into the list
item=[bug,assign,descrip,date]
#added item to the list
report.append(item)
#passing list through Pandas DataFreame
jira=pd.DataFrame(report)
#export the data into excel sheet
jira.to_csv("file.csv",index=False)

   