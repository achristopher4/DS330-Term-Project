## FIFA Analysis
## Author: Alexander Christopher
## Date: 04/22/2022

## OS Path: cd Desktop/330_Project

import numpy as np
import pandas as pd
import os
import requests
import lxml.html as lh

# Retrieving the data from the Data folder

data_path = "/Users/alexchristopher/Desktop/330_Project/Python_Code/Data/"
player_path = data_path+"Raw/players_21.csv"
Players_Data = pd.read_csv(player_path)

players_columns = ['short_name', 'long_name', 'age', 'dob', 'height_cm', 'weight_kg',
            'nationality', 'club_name', 'league_name', 'league_rank', 'overall',
            'potential', 'wage_eur', 'player_positions', 'preferred_foot',
            'international_reputation', 'weak_foot', 'skill_moves', 'work_rate',
            'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']

Players_Data = Players_Data[players_columns]

# Web scraping top scorers from the champions league
    # Code adopted from: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059

url = "https://www.sportingnews.com/us/soccer/news/champions-league-top-goal-scorer-golden-boot-ranking/1qqfqkj1d8uf31cb26ocmrmuuk"
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')

tr_elements = doc.xpath('//tr')
col=[]
i=0
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    #print('%d:"%s"'%(i,name))
    col.append((name,[]))

for j in range(1,len(tr_elements)):
    T=tr_elements[j]
    if len(T)!=7:
        break
    i=0
    for t in T.iterchildren():
        data=t.text_content()
        if i>0:
            try:
                data=int(data)
            except:
                pass
        col[i][1].append(data)
        i+=1

Dict={title:column for (title,column) in col}
Goal_Data = pd.DataFrame(Dict)
goal_columns = list(Goal_Data)

data_inter_path = data_path + "Intermediate/"

Players_Data.to_csv(data_inter_path+"Players_Data")
Goal_Data.to_csv(data_inter_path+"Goal_Data")
