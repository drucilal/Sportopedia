import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os

# NBA Data Sources
nba_team = dd.read_csv('s3://sportsdatawarehouse/NBA/teams/NBA_teams_team stats_*.csv').compute()
nba_player = dd.read_csv('s3://sportsdatawarehouse/NBA/players/NBA_Players_per game stats_*.csv').compute()
nba_salary = dd.read_csv('s3://sportsdatawarehouse/NBA/salary/*nbasalary.csv').compute()
nba_teamid = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/nba_team.csv').compute()
nba_playerid = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/nba_players.csv').compute()
nba_game_details = dd.read_csv('s3://sportsdatawarehouse/NBA/games_details.csv').compute()
# WNBA Data Sources
wnba_team = dd.read_csv('s3://sportsdatawarehouse/WNBA/team/wbna_team*.csv').compute()
wnba_player = dd.read_csv('s3://sportsdatawarehouse/WNBA/players/wbna_player*.csv').compute()
wnba_salary = dd.read_csv('s3://sportsdatawarehouse/WNBA/salaries/*_team_salaries.csv').compute()
wnba_teamid = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/wnba_team.csv').compute()
wnba_playerid = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/wnba_players.csv').compute()

# Men College Basketball
ncam_players = dd.read_csv(
    's3://sportsdatawarehouse/NCAAmen/men_ncaa_data/DataFiles/playbyplay/files/Players_*.csv').compute()
ncam_cities = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_cities.csv').compute()
ncam_coaches = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_coaches.csv').compute()
ncam_conference = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_conference.csv').compute()
ncam_conference_games = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_confgames.csv').compute()
ncam_gamecities = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_gamecities.csv').compute()
ncam_seasongames = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_season_games.csv').compute()
ncam_teamconference = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tconf.csv').compute()
ncam_teams = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_teams.csv').compute()
ncam_tournament = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tournament.csv').compute()

# Women College Basketball
ncaw_players = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/data/WPlayers.csv').compute()
ncaw_cities = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_cities.csv').compute()
ncaw_conference = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_conference.csv').compute()
ncaw_gamecities = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_gamecities.csv').compute()
ncaw_seasongames = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_season_games.csv').compute()
ncaw_season = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_seasons.csv').compute()
ncaw_teamconference = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tconf.csv').compute()
ncaw_teams = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_teams.csv').compute()
ncaw_tournament = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tournament.csv').compute()

# MLB Data Sources

mlb_players = dd.read_csv('s3://sportsdatawarehouse/MLB/mlb_players.csv').compute()
mlb_teams = dd.read_csv('s3://sportsdatawarehouse/MLB/mlb_teams.csv',dtype={'DivWin': 'object',
       'WCWin': 'object',
       'divID': 'object'}).compute()
mlb_allstars = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AllstarFull.csv').compute()
mlb_appearances = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Appearances.csv',
                              dtype={'G_dh': 'float64'}).compute()
mlb_awardmanagers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsManagers.csv').compute()
mlb_awardplayers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsShareManagers.csv').compute()
mlb_awardshared_players = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsShareManagers.csv').compute()
mlb_batting = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Batting.csv').compute()
mlb_postbatting = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/BattingPost.csv').compute()
mlb_college = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/CollegePlaying.csv').compute()
mlb_fielding = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Fielding.csv',
                           dtype={'E': 'float64', 'InnOuts': 'float64'}).compute()
mlb_fieldingof = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/FieldingOF.csv').compute()
mlb_fieldingof = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/FieldingOF.csv').compute()
mlb_fieldingpost = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/FieldingPost.csv').compute()
mlb_halloffame = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/HallOfFame.csv').compute()
mlb_homegames = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/HomeGames.csv').compute()
mlb_managers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Managers.csv').compute()
mlb_halfmanagers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/ManagersHalf.csv').compute()
mlb_parks = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Parks.csv').compute()
mlb_players = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/People.csv').compute()
mlb_pitching = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Pitching.csv',
                           dtype={'BFP': 'float64'}).compute()
mlb_postpitching = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/PitchingPost.csv').compute()
mlb_salaries = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Salaries.csv').compute()
mlb_postseries = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/SeriesPost.csv').compute()
mlb_teams = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Teams.csv', dtype={'DivWin': 'object',
                                                                                   'WCWin': 'object',
                                                                                   'divID': 'object'}).compute()
mlb_teams_franch = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/TeamsFranchises.csv').compute()
mlb_halfteams = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/TeamsHalf.csv').compute()

# women soccer
wsoccer_stadium = dd.read_csv('s3://sportsdatawarehouse/women_soccer/stadium_info.csv').compute()
wsoccer_fieldplayer = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_fieldplayer.csv').compute()
wsoccer_goal = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_goal.csv').compute()
wsoccer_player = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_player.csv').compute()
wsoccer_playfield = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_playfield.csv').compute()
wsoccer_playstats = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_playstats.csv').compute()
wsoccer_franch = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccerfranchises.csv').compute()
wsoccer_games_r = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccergameresults.csv').compute()
wsoccer_teams = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccerteam_stats.csv').compute()

# NFL Football & Superbowl Data Sources
afc = dd.read_csv('s3://sportsdatawarehouse/NFL_f/AFC_records.CSV').compute()
afl = dd.read_csv('s3://sportsdatawarehouse/NFL_f/AFL_records.CSV').compute()
defense_game_stat = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_GAME_STATS.CSV').compute()
defense_intecep = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_INTERCEPTIONS.CSV').compute()
defense_pass = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_PASSING.CSV').compute()
defense_rece = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_RECEIVING.CSV').compute()
defense_rush = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_RUSHING.CSV').compute()
defense_score = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_SCORING.CSV').compute()
defense_tackle = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Defense_TACKLES.CSV').compute()
nfc = dd.read_csv('s3://sportsdatawarehouse/NFL_f/NFC_records.CSV').compute()
nfl_records = dd.read_csv('s3://sportsdatawarehouse/NFL_f/NFL_records.CSV').compute()
offense_field = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_FIELD_GOALS.CSV').compute()
offense_game_stat = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_GAME_STATS.CSV').compute()
offense_kicking = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_KICKING.CSV').compute()
offense_kick_return = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_KICK_RETURNS.CSV').compute()
offense_offensive_line = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_OFFENSIVE_LINE.CSV').compute()
offence_pass = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_PASSING.CSV').compute()
offense_pun = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_PUNTING.CSV').compute()
offense_rece = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_RECEIVING.CSV').compute()
offense_rush = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_RECEIVING.CSV').compute()
offense_score = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_SCORING.CSV').compute()
offense_touch = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Offense_TOUCHDOWNS.CSV').compute()
merged = dd.read_csv('s3://sportsdatawarehouse/NFL_f/clean_offense_def.csv',
                     dtype={'Defense_passing_1stpct': 'float64',
                            'Defense_rushing_1stpct': 'float64',
                            'Offense_kicking_Avg': 'float64',
                            'Offense_kicking_Pct': 'float64',
                            'Offense_kicking_returns_Avg': 'float64',
                            'Offense_passing_1stpct': 'float64',
                            'Offense_punting_Net_Avg': 'float64',
                            'Offense_rushing_1stpct': 'float64'}).compute()
superbowl = dd.read_csv('s3://sportsdatawarehouse/NFL_f/Superbowl_winners.CSV').compute()
