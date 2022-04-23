## FIFA Analysis: Clean Up DataFrame
## Author: Alexander Christopher
## Date: 04/22/2022

import numpy as np
import pandas as pd
import os

data_path = "/Users/alexchristopher/Desktop/330_Project/Python_Code/Data/"

Players = pd.read_csv(data_path+"Intermediate/Players_Data.csv")
Goals = pd.read_csv(data_path+"Intermediate/Goal_Data.csv")
Players = Players.drop(columns = 'Unnamed: 0')
Goals = Goals.drop(columns = 'Unnamed: 0')

print('\nGoals')
print(Goals.head(15))

# Cleaning and Modifying the Goals and Players Dataset
## Removing period from rank


## Filling in blank ranks with appropriate rank


## Removing PK from Goals attribute


## Adjusting players names from Goals so they are the same as the names from PLayers


## Adjusting team names from Goals so they are the same as the names from PLayers


## Replacing NaN values in Players with 0





print('Players')
print(Players.head())
