import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
import functions_file
import sport_files
from functions_file import *
from sport_files import * 
import processing
from processing import *

# Transfer to postgres database
transfer_tosql(nba_full_team,'nba_teams')
transfer_tosql(wnba_players_info,'wnba_players')
transfer_tosql(wnba_team_details,'wnba_teams')
transfer_tosql(mlb_player_details,'mlb_players')
transfer_tosql(mlb_stadiums,'mlb_stadiums')
transfer_tosql(mlb_batting_details,'mlb_batting')
transfer_tosql(mlb_pitching_details,'mlb_pitching')
transfer_tosql(mlb_fielding_details,'mlb_fielding')
transfer_tosql(mlb_allstar_details,'mlb_allstars')
transfer_tosql(mlb_halloffame_details,'mlb_halloffame')
transfer_tosql(mlb_teams,'mlb_teams')
transfer_tosql(ncam_team_details,'ncaam_team')
transfer_tosql(ncam_conference_info,'ncam_conferences')
transfer_tosql(ncam_gamecities_info,'ncam_citygames')
transfer_tosql(ncam_seasongames,'ncam_seasongames')
transfer_tosql(ncam_tournament,'ncam_tournaments')
transfer_tosql(ncam_conference_games,'ncam_conferencegames')
transfer_tosql(ncaw_team_details,'ncaaw_teams')
transfer_tosql(ncaw_players,'ncaaw_players')
transfer_tosql(ncaw_cities,'ncaaw_cities')
transfer_tosql(ncaw_game_cities,'ncaaw_citygames')
transfer_tosql(ncaw_seasongames,'ncaaw_seasongames')
transfer_tosql(ncaw_teamconference,'ncaaw_conference')
transfer_tosql(mls_final_players,'mls_players')
transfer_tosql(mls_teams,'mls_teams')
transfer_tosql(nfl,'nfl')
transfer_tosql(superbowl,'superbowl')
