import numpy as np 
import pandas as pd 
import os 

import warnings 
warnings.filterwarnings('ignore')

df = pd.read_csv('soccerData.csv')

df['date']= pd.to_datetime(df['date'])

raw_match_stats = df[[
                'date',
                'match_id',
                'home_team_name',
                'away_team_name',
                'home_team_goal_count', 
                'away_team_goal_count',
                'home_team_half_time_goal_count',
                'away_team_half_time_goal_count',
                'home_team_shots',
                'away_team_shots',
                'home_team_shots_on_target',
                'away_team_shots_on_target',
                'home_team_fouls',
                'away_team_fouls',
                'home_team_corner_count',
                'away_team_corner_count',
                'home_team_yellow',
                'away_team_yellow',
                'home_team_red',
                'away_team_red'
                ]]

raw_match_stats = raw_match_stats.sort_values(by=['date'], ascending=False)

raw_match_stats = raw_match_stats.dropna(inplace=True)
