## FIFA Analysis: Importing and Filtering Raw Data
## Author: Alexander Christopher
## Date: 04/22/2022

import numpy as np
import pandas as pd
import os
from pandas.core.dtypes.common import is_numeric_dtype

# Retrieving the data from the Raw Data folder
data_path = "/Users/alexchristopher/Desktop/330_Project/Python_Code/Data/"
player_path = data_path+"Raw/players_20.csv"
Players = pd.read_csv(player_path)

players_columns = ['short_name', 'long_name', 'age', 'dob', 'height_cm', 'weight_kg',
            'nationality', 'club_name', 'league_name', 'league_rank', 'overall',
            'potential', 'wage_eur', 'player_positions', 'preferred_foot',
            'international_reputation', 'weak_foot', 'skill_moves', 'work_rate',
            'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']

Players = Players[players_columns]


goals_path = data_path + "Raw/Goals_2020.csv"
Goals = pd.read_csv(goals_path)

goals_columns = ['League', 'Team', 'Player', 'Position', 'Appearances', 'Goals', 'Started',
                'Started As A Sub', 'Came On', 'Taken Off', 'Own Goals', 'Type Of Goal',
                'First Half', 'Second Half', 'First Scorer', 'Last Scorer', 'Home', 'Away',
                'Right Foot', 'Left Foot', 'Header', 'Other Method', 'Open Play', 'Cross', 'Free Kick',
                'Direct Free Kick', 'Throw In', 'Penalty', 'Corner','Assists', '% Assists',
                '% Clean Sheets', 'Hat Tricks']
Goals = Goals[goals_columns]


print('Players')
print(Players.head(15))

print('\nGoals')
print(Goals.head(15))

# Making the attributes names the same in both datasets where applicable
Players = Players.rename(columns={"club_name":"Team", "league_name":"League", "player_positions":"FIFA Position"})

# Cleaning and Modifying the Goals and Players Dataset
## Removing Null player values from Goals
Goals = Goals.dropna(subset = ['Player'])
## Removing Null Team values from Players
Players = Players.dropna(subset = ['League'])

## Removing Goal Keepers from Goals
Goals = Goals[Goals['Position'] != "Goalkeeper"]

## Add columns Goals, Position, and Appearances to Players Dataframe
Players["Goals"] = pd.NaT
Players["General_Position"] = pd.NaT
Players["Appearances"] = pd.NaT

## Add index column to Players DataFrame
Players["Index"] = Players.index

# Split Goals Player name into first and last name
size = Goals.shape[0]
#size = 20
for x in range(size):
  name = Goals['Player'].iloc[x]
  name_split = name.split(' ')
  first_and_last = [name_split[0], name_split[-1]]
  team = Goals['Team'].iloc[x]
  goals, appearances, position = Goals['Goals'].iloc[x], Goals['Appearances'].iloc[x], Goals['Position'].iloc[x]

  last_name = Players.loc[Players["short_name"].str.contains(first_and_last[-1], case = False)]
  first_name = last_name.loc[last_name["short_name"].str.contains(first_and_last[0], case = False)]

  ## Check to see if query produced any results
  if last_name.shape[0] >= 1:
    if last_name.shape[0] == 1:
      ## Query produced exactly one result
      ## Add information
      p_index = last_name["Index"].values[0]
      Players.loc[Players["Index"] == p_index, "Goals"] = goals
      Players.loc[Players["Index"] == p_index, "Appearances"] = appearances
      Players.loc[Players["Index"] == p_index, "General_Position"] = position
    elif last_name.shape[0] > 1:
      ## Query for players with the team == to the variable team
      team_name = last_name.loc[last_name['Team'].str.contains(team, case = False)]
      if team_name.shape[0] == 1:
        ## Query produced exactly one result
        ## Add information
        p_index = team_name["Index"].values[0]
        Players.loc[Players["Index"] == p_index, "Goals"] = goals
        Players.loc[Players["Index"] == p_index, "Appearances"] = appearances
        Players.loc[Players["Index"] == p_index, "General_Position"] = position
      elif team_name.shape[0] > 1:
        ## Further subsquery for players with the last_name, team, and first_name equal to parameters
        first_name_team = team_name.loc[team_name["short_name"].str.contains(first_and_last[0], case = False)]
        if first_name_team.shape[0] == 1:
          ## Query produced exactly one result
          ## Add information
          p_index = first_name_team["Index"].values[0]
          Players.loc[Players["Index"] == p_index, "Goals"] = goals
          Players.loc[Players["Index"] == p_index, "Appearances"] = appearances
          Players.loc[Players["Index"] == p_index, "General_Position"] = position
  elif last_name.shape[0] == 0:
    ## Last_name produced no results, try searching for player's first_name first
    if first_name.shape[0] == 1:
      p_index = first_name["Index"].values[0]
      Players.loc[Players["Index"] == p_index, "Goals"] = goals
      Players.loc[Players["Index"] == p_index, "Appearances"] = appearances
      Players.loc[Players["Index"] == p_index, "General_Position"] = position
    elif first_name.shape[0] > 1:
      ## Further subquerying for player with first_name and team name in Players DataFrame
      first_team = first_name.loc[first_name['Team'].str.contains(team, case = False)]
      if first_team.shape[0] == 1:
        ## Query produced exactly one result
        ## Add information
        p_index = first_team["Index"].values[0]
        Players.loc[Players["Index"] == p_index, "Goals"] = goals
        Players.loc[Players["Index"] == p_index, "Appearances"] = appearances
        Players.loc[Players["Index"] == p_index, "General_Position"] = position

## Test
#print(Players.loc[Players["Team"].str.contains("Barce",case = False)].head())

## Drop all players that did not receive Goals, Appearance, or Position attribute
Players = Players.dropna(subset = ['Goals'])

# Fill Null Numeric Values with 0
## Check which columns have nan in columns
check_columns = list(Players)
for cn in check_columns:
  if Players[cn].isnull().values.any():
    ## Check whether column is numeric
    if is_numeric_dtype(Players[cn]):
      ## Fill NaN with 0
      Players[cn] = Players[cn].fillna(0)

# Export Players DataFrame to the folder Intermediate
Players.to_csv('/Users/alexchristopher/Desktop/330_Project/Python_Code/Data/Intermediate/intermediate_players.csv')
