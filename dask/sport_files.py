import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import os
import functions_file
from functions_file import *

"""
Files retrieved from S3 bucket
"""
# NBA Files

nba_team = read_files('s3://sportsdatawarehouse/NBA/teams/NBA_teams_team stats_*.csv')
nba_player = read_files('s3://sportsdatawarehouse/NBA/players/NBA_Players_per game stats_*.csv')
nba_salary = read_files('s3://sportsdatawarehouse/NBA/salary/*nbasalary.csv')
nba_teamid = read_files('s3://sportsdatawarehouse/key_identifiers/nba_teamID.csv')
nba_playerid = read_files('s3://sportsdatawarehouse/key_identifiers/nba_players.csv')
nba_game_details= read_files('s3://sportsdatawarehouse/NBA/games_details.csv')
nba_player_info = read_files('s3://sportsdatawarehouse/NBA/players_info.csv')


# WNBA files
wnba_team = read_files('s3://sportsdatawarehouse/WNBA/team/wbna_team*.csv')
wnba_player =  read_files('s3://sportsdatawarehouse/WNBA/players/wbna_player*.csv')
wnba_salary =  read_files('s3://sportsdatawarehouse/WNBA/salaries/*_team_salaries.csv')
wnba_teamid =  read_files('s3://sportsdatawarehouse/key_identifiers/wnba_team.csv')
wnba_playerid =  read_files('s3://sportsdatawarehouse/key_identifiers/wnba_players.csv')

# College Men Basketball
ncam_players =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/DataFiles/playbyplay/files/Players_*.csv')
ncam_cities =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_cities.csv')
ncam_coaches =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_coaches.csv')
ncam_conference =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_conference.csv')
ncam_conference_games =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_confgames.csv')
ncam_gamecities =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_gamecities.csv')
ncam_seasongames =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_season_games.csv')
ncam_team_conf =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tconf.csv')
ncam_teams =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_teams.csv')
ncam_tournament =  read_files('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tournament.csv')

# College Women Basketball

ncaw_players =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/data/WPlayers.csv')
ncaw_cities =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_cities.csv')
ncaw_conference =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_conference.csv')
ncaw_game_cities =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_gamecities.csv')
ncaw_seasongames =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_season_games.csv')
ncaw_season =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_seasons.csv')
ncaw_teamconference =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tconf.csv')
ncaw_teams =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_teams.csv')
ncaw_tournament =  read_files('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tournament.csv')

# MLB Baseball Dataset
mlb_teams = read_files_datatypes('s3://sportsdatawarehouse/MLB/mlb_teams.csv',dtype={'DivWin': 'object',
       'WCWin': 'object',
       'divID': 'object'})
mlb_appearances = read_files_datatypes('s3://sportsdatawarehouse/MLB/2019/core/Appearances.csv',
                              dtype={'G_dh': 'float64'})
mlb_fielding = read_files_datatypes('s3://sportsdatawarehouse/MLB/2019/core/Fielding.csv',
                           dtype={'E': 'float64', 'InnOuts': 'float64'})

mlb_pitching = read_files_datatypes('s3://sportsdatawarehouse/MLB/2019/core/Pitching.csv',
                           dtype={'BFP': 'float64'})

mlb_teams = read_files_datatypes('s3://sportsdatawarehouse/MLB/2019/core/Teams.csv', dtype={'DivWin': 'object',
                                                                                   'WCWin': 'object',
                                                                                   'divID': 'object'})

mlb_players = read_files('s3://sportsdatawarehouse/MLB/mlb_players.csv')
mlb_allstars = read_files('s3://sportsdatawarehouse/MLB/2019/core/AllstarFull.csv')
mlb_awardmanagers = read_files('s3://sportsdatawarehouse/MLB/2019/core/AwardsManagers.csv')
mlb_awardplayers = read_files('s3://sportsdatawarehouse/MLB/2019/core/AwardsShareManagers.csv')
mlb_awardshared_players = read_files('s3://sportsdatawarehouse/MLB/2019/core/AwardsShareManagers.csv')
mlb_batting = read_files('s3://sportsdatawarehouse/MLB/2019/core/Batting.csv')
mlb_postbatting = read_files('s3://sportsdatawarehouse/MLB/2019/core/BattingPost.csv')
mlb_college = read_files('s3://sportsdatawarehouse/MLB/2019/core/CollegePlaying.csv')
mlb_fieldingof = read_files('s3://sportsdatawarehouse/MLB/2019/core/FieldingOF.csv')
mlb_fieldingof = read_files('s3://sportsdatawarehouse/MLB/2019/core/FieldingOF.csv')
mlb_fieldingpost = read_files('s3://sportsdatawarehouse/MLB/2019/core/FieldingPost.csv')
mlb_halloffame = read_files('s3://sportsdatawarehouse/MLB/2019/core/HallOfFame.csv')
mlb_homegames = read_files('s3://sportsdatawarehouse/MLB/2019/core/HomeGames.csv')
mlb_managers = read_files('s3://sportsdatawarehouse/MLB/2019/core/Managers.csv')
mlb_halfmanagers = read_files('s3://sportsdatawarehouse/MLB/2019/core/ManagersHalf.csv')
mlb_parks = read_files('s3://sportsdatawarehouse/MLB/2019/core/Parks.csv')
mlb_players = read_files('s3://sportsdatawarehouse/MLB/2019/core/People.csv')

mlb_postpitching = read_files('s3://sportsdatawarehouse/MLB/2019/core/PitchingPost.csv')
mlb_salaries = read_files('s3://sportsdatawarehouse/MLB/2019/core/Salaries.csv')
mlb_postseries = read_files('s3://sportsdatawarehouse/MLB/2019/core/SeriesPost.csv')

mlb_teams_franch = read_files('s3://sportsdatawarehouse/MLB/2019/core/TeamsFranchises.csv')
mlb_halfteams = read_files('s3://sportsdatawarehouse/MLB/2019/core/TeamsHalf.csv')

# NFL Data
nfl = read_files_datatypes('s3://sportsdatawarehouse/NFL_f/clean_offense_def.csv',
                     dtype={'Defense_passing_1stpct': 'float64',
                            'Defense_rushing_1stpct': 'float64',
                            'Offense_kicking_Avg': 'float64',
                            'Offense_kicking_Pct': 'float64',
                            'Offense_kicking_returns_Avg': 'float64',
                            'Offense_passing_1stpct': 'float64',
                            'Offense_punting_Net_Avg': 'float64',
                            'Offense_rushing_1stpct': 'float64'})
superbowl = read_files('s3://sportsdatawarehouse/NFL_f/Superbowl_winners.CSV')