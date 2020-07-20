import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
from functions_file import *
from sport_files import *

"""
Data Manipulation
"""

# NBA

# Merge players and teams dataset togehter
players = merge_columns(nba_player_info,nba_player,'Player')
players_teams = merge_columns(players,nba_teamid,'Tm')
player_teams_s = merge_columns(players_teams,nba_salary,['Player','Team','season'])
# Remove percentage sign
nba_full_team = remove_percent_signs(player_teams_s)

# WNBA
wnba_team_info = merge_columns(wnba_team,wnba_salary,['Team','season'])
wnba_players_info = merge_columns(wnba_teamid,wnba_player,'Tm')
wnba_team_details = remove_percent_signs(wnba_team_info)

# MLB
# MLB Players
mlb_players_info = merge_columns(mlb_players,mlb_salaries,'playerID')
mlb_player_school_info = merge_columns(mlb_players_info,mlb_college,'playerID')
mlb_player_details = merge_columns(mlb_player_school_info,mlb_schools,'schoolID')

# MLB Stadium 
mlb_stadiums = merge_columns(mlb_homegames,mlb_parks,'park.key')


# Extract Players IDs
mlb_players_ids = mlb_players[['playerID','nameFirst','nameLast']]
mlb_teams_id = mlb_teams[['teamID','name']]

mlb_batting_details  = add_unique_ids(mlb_batting)
mlb_pitching_details = add_unique_ids(mlb_pitching)
mlb_fielding_details = add_unique_ids(mlb_fielding)
mlb_allstar_details = add_unique_ids(mlb_allstars)
mlb_halloffame_details = merge_columns(mlb_halloffame,mlb_players_ids,'playerID')



