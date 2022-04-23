## FIFA Analysis: Clean Up DataFrame
## Author: Alexander Christopher
## Date: 04/22/2022

import numpy as np
import pandas as pd
import os

data_path = "/Users/alexchristopher/Desktop/330_Project/Python_Code/Data/"

Players = pd.read_csv(data_path+"Intermediate/Players_Data.csv")
Goals = pd.read_csv(data_path+"Intermediate/Goal_Data.csv")

Players = PLayers.drop(columns = 'Unnamed: 0')
Goals = Goals.drop(columns = 'Unnamed: 0')

print('Players')
print(Players.head())
print('\nGoals')
print(Goals.head(15))
