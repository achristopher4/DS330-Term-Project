## FIFA Analysis: Importing and Filtering Raw Data
## Author: Alexander Christopher
## Date: 04/22/2022

import numpy as np
import pandas as pd
import os


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


goals_path = data_path + "Raw/Goals_2020.csv"
Goals_Data = pd.read_csv(goals_path)

goals_columns = ['League', 'Team', 'Player', 'Position', 'Appearances', 'Goals', 'Started',
                'Started As A Sub', 'Came On', 'Taken Off', 'Own Goals', 'Type Of Goal',
                'First Half', 'Second Half', 'First Scorer', 'Last Scorer', 'Home', 'Away',
                'Right Foot', 'Left Foot', 'Header', 'Other Method', 'Open Play', 'Cross', 'Free Kick',
                'Direct Free Kick', 'Throw In', 'Penalty', 'Corner','Assists', '% Assists',
                '% Clean Sheets', 'Hat Tricks']
Goals_Data = Goals_Data[goals_columns]

print('\nGoals')
print(Goals_Data.sort_values('Player').head(15))

# Cleaning and Modifying the Goals and Players Dataset
## Removing Null player values from Goals_Data


## Removing players from Goals_Data not in Players_Data


## Replacing NaN values with 0





print('Players')
print(Players_Data.sort_values('long_name').head(15))
