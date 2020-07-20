import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
from files import *
from config import *


def remove_pct(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.replace('%', 'pct')
    df = df.fillna(0.0)
    # df = df.drop('Unnamed: 0', axis=1)
    return df


def merge_columns(df1, df2, *cols):
    for col in cols:
        data = dd.merge(df1, df2, on=col)
        # data = data.drop('Unnamed: 0', axis=1)
    return data


def drop_values(df):
    data = df.dropna()
    return data


def transfer_tosql(df, table_name):
    engine = sqlalchemy.create_engine()
    con = engine.connect()
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    return con.close()


nba_teams = remove_pct(nba_team)
nba_players = remove_pct(nba_player)
nba_game_d = drop_values(nba_game_details)
wnba_teams = remove_pct(wnba_team)
wnba_teams.rename(columns={'Western Conference': 'Team'}, inplace=True)
wnba_players = remove_pct(wnba_player)

nba_teams_merged = merge_columns(nba_teamid, nba_teams, 'Team')
nba_players_merged = merge_columns(nba_playerid, nba_players, 'Player')
wnba_teams_merged = merge_columns(wnba_teamid, wnba_teams, 'Team')
wnba_players_merged = merge_columns(wnba_playerid, wnba_players, 'Player')
nba_salaries = nba_salary
wnba_salaries = wnba_salary

# Melt Dataframes
nba_team_reshaped = nba_teams_merged.melt(id_vars=['Team', 'season'],
                                          var_name='statistic_name', value_name='statistic')
nba_players_reshaped = nba_players_merged.melt(id_vars=['Player', 'Pos', 'Age', 'Tm', 'season'],
                                               var_name='statistic_name', value_name='statistic')
wnba_team_reshaped = wnba_teams_merged.melt(id_vars=['Team', 'season'],
                                            var_name='statistic_name', value_name='statistic')
wnba_player_reshaped = wnba_players_merged.melt(id_vars=['Player', 'Tm', 'Pos', 'season'],
                                                var_name='statistic_name', value_name='statistic')

# College Ball
men_players = drop_values(ncam_players)
men_cities = drop_values(ncam_cities)
men_coaches = drop_values(ncam_coaches)
men_conference = drop_values(ncam_conference)
men_conference_games = drop_values(ncam_conference_games)
men_seasongames = drop_values(ncam_seasongames)
men_teamconference = drop_values(ncam_teamconference)
men_teams = drop_values(ncam_teams)
men_tournament = drop_values(ncam_tournament)
women_players = drop_values(ncaw_players)
women_cities = drop_values(ncaw_cities)
women_conference = drop_values(ncaw_conference)
women_gamecities = drop_values(ncaw_gamecities)
women_seasongames = drop_values(ncaw_seasongames)
women_season = drop_values(ncaw_season)
women_teamconference = drop_values(ncaw_teamconference)
women_teams = drop_values(ncaw_teams)
women_tournament = drop_values(ncaw_tournament)

# MLB Baseball
fill_star = {'startingPos': 0.0}
mlb_allstar = mlb_allstars.fillna(fill_star)
mlb_allstar = mlb_allstar.dropna(subset=['yearID', 'gameNum', 'gameID'])
fill2 = {'lgID': 'n', 'GS': 0.0, 'G_defense': 0.0, 'G_dh': 0.0, 'G_ph': 0.0, 'G_pr': 0.0}
mlb_appearance = mlb_appearances.fillna(fill2)
mlb_awardmanager = mlb_awardmanagers.fillna({'tie': 'none', 'notes': 'none'})
mlb_awardplayer = mlb_awardplayers.fillna({'pointsMax': 0.0})
mlb_awardshared_player = mlb_awardshared_players.fillna({'votesFirst': 0.0})
mlb_bat = mlb_batting.fillna({'lgID': 'n', 'RBI': 0.0, 'SB': 0.0, 'CS': 0.0, 'SO': 0.0,
                              'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0, 'SF': 0.0, 'GIDP': 0.0})
mlb_postbat = mlb_postbatting.fillna({'CS': 0.0, 'HBP': 0.0, 'SH': 0.0, 'SF': 0.0, 'GIDP': 0.0})
mlb_field = mlb_fielding.fillna({'lgID': 'n', 'GS': 0.0, 'InnOuts': 0.0, 'PB': 0.0, 'WP': 0.0, 'SB': 0.0,
                                 'CS': 0.0, 'ZR': 0.0})
mlb_fieldof = mlb_fieldingof.fillna({'Glf': 0.0, 'Gcf': 0.0, 'Grf': 0.0})
mlb_fieldpost = mlb_fieldingpost.fillna({'PB': 0.0, 'SB': 0.0, 'CS': 0.0})

mlb_fame = mlb_halloffame.fillna({'ballots': 0.0, 'needed': 0.0, 'votes': 0.0, 'needed_note': 'none'})

mlb_homegame = mlb_homegames.fillna({'league.key': 'n'})

mlb_manager = mlb_managers.fillna({'lgID': 'n', 'plyrMgr': 'N'})
mlb_park = mlb_parks.fillna({'park.alias': 'none', 'country': 'n'})
mlb_player = mlb_players.fillna({'birthYear': 0.0, 'birthMonth': 0.0, 'birthDay': 0.0, 'birthCountry': 'none',
                                 'birthState': 'none', 'birthCity': 'none', 'deathYear': 0.0, 'deathMonth': 0.0,
                                 'deathCountry': 'none', 'deathState': 'none', 'deathCity': 'none',
                                 'nameFirst': 'unknown', 'nameGiven': 'unknown', 'weight': 0.0, 'height': 0.0,
                                 'bats': 'n', 'throws': 'n'})
mlb_player = mlb_player.dropna(subset=['debut', 'finalGame', 'retroID', 'bbrefID'])
mlb_pitch = mlb_pitching.fillna({'lgID': 'n', 'BAOpp': 0.0, 'ERA': 0.0, 'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0,
                                 'SF': 0.0, 'GIDP': 0.0})
mlb_postpitch = mlb_postpitching.fillna(
    {'WP': 0.0, 'BK': 0.0, 'BFP': 0.0, 'BAOpp': 0.0, 'ERA': 0.0, 'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0,
     'SF': 0.0, 'GIDP': 0.0})
mlb_team = mlb_teams.fillna(
    {'lgID': 'n', 'divID': 'n', 'Ghome': 0.0, 'DivWin': 'n', 'WCWin': 'n', 'LgWin': 'n', 'WSWin': 'n',
     'BB': 0.0, 'SO': 0.0, 'SB': 0.0, 'CS': 0.0, 'HBP': 0.0, 'SF': 0.0, 'park': 'n', 'attendance': 0.0})

# Women Soccer
wsoc_stadium = wsoccer_stadium
wsoc_fieldplayer = wsoccer_fieldplayer
wsoc_goal = wsoccer_goal
wsoc_player = wsoccer_player
wsoc_playfield = wsoccer_playfield
wsoc_playstat = wsoccer_playstats
wsoc_franch = wsoccer_franch
wsoc_games_r = wsoccer_games_r
wsoc_teams = wsoccer_teams

# NFL
afc_rec = drop_values(afc)
afl_rec = drop_values(afl)
d_game_stat = drop_values(defense_game_stat)
d_intecep = drop_values(defense_intecep)
d_pass = drop_values(defense_pass)
d_receive = drop_values(defense_rece)
defense_r = drop_values(defense_rush)
defense_s = drop_values(defense_score)
d_tackle = drop_values(defense_tackle)
nfc_rec = drop_values(nfc)
nfl_rec = drop_values(nfl_records)
o_field = drop_values(offense_field)
o_game = drop_values(offense_game_stat)
o_k = drop_values(offense_kicking)
off_kickreturn = drop_values(offense_kick_return)
off_line = drop_values(offense_offensive_line)
of_pass = drop_values(offence_pass)
of_pun = drop_values(offense_pun)
of_rece = drop_values(offense_rece)
off_rush = drop_values(offense_rush)
off_score = drop_values(offense_score)
off_touch = drop_values(offense_touch)
merg_data = drop_values(merged)
superb = drop_values(superbowl)


# Transfer Data to Postgres
def transfer_tosql(df, table_name):
    engine = sqlalchemy.create_engine(url)
    con = engine.connect()
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    return con.close()


# American Football

transfer_tosql(afc_rec, 'afc_records')
transfer_tosql(afl_rec, 'afl_records')
transfer_tosql(d_game_stat, 'defense_gamestatistics')
transfer_tosql(d_intecep, 'defense_interception')
transfer_tosql(d_pass, 'defense_pass')
transfer_tosql(d_receive, 'defense_receive')
transfer_tosql(defense_r, 'defense_rush')
transfer_tosql(defense_s, 'defense_score')
transfer_tosql(nfc_rec, 'nfc_records')
transfer_tosql(nfl_rec, 'nfl_records')
transfer_tosql(o_field, 'offense_fieldgoals')
transfer_tosql(o_game, 'offense_game_stats')
transfer_tosql(o_k, 'offense_kicks')
transfer_tosql(off_kickreturn, 'offense_kickreturns')
transfer_tosql(off_line, 'offense_line')
transfer_tosql(of_pass, 'offense_passing')
transfer_tosql(of_pun, 'offense_punting')
transfer_tosql(of_rece, 'offense_receiving')
transfer_tosql(off_rush, 'offense_rushing')
transfer_tosql(off_score, 'offense_score')
transfer_tosql(off_touch, 'offense_touch')
transfer_tosql(merg_data, 'offense_defense')
transfer_tosql(superb, 'superbowl')
transfer_tosql(nba_game_d, 'nba_game_details')

# Basketball
transfer_tosql(nba_team_reshaped, 'nba_teams')
transfer_tosql(wnba_team_reshaped, 'wnba_teams')
transfer_tosql(nba_players_reshaped, 'nba_players')
transfer_tosql(wnba_player_reshaped, 'wnba_players')
transfer_tosql(nba_salaries, 'nba_salary')
transfer_tosql(wnba_salaries, 'wnba_salary')

# MLB Baseball

transfer_tosql(mlb_allstar, 'mlb_allstar_games')
transfer_tosql(mlb_appearance, 'mlb_appearances')
transfer_tosql(mlb_awardmanager, 'mlb_awardmanagers')
transfer_tosql(mlb_awardplayer, 'mlb_awardplayers')
transfer_tosql(mlb_awardshared_player, 'mlb_awardsharedplayers')
transfer_tosql(mlb_bat, 'mlb_batting')
transfer_tosql(mlb_postbat, 'mlb_postbatting')
transfer_tosql(mlb_field, 'mlb_fielding')
transfer_tosql(mlb_fieldof, 'mlb_fieldingof')
transfer_tosql(mlb_fieldpost, 'mlb_fieldingpost')
transfer_tosql(mlb_fame, 'mlb_halloffames')
transfer_tosql(mlb_homegame, 'mlb_homegames')
transfer_tosql(mlb_manager, 'mlb_managers')
transfer_tosql(mlb_park, 'mlb_parks')
transfer_tosql(mlb_player, 'mlb_players')
transfer_tosql(mlb_pitch, 'mlb_pitching')
transfer_tosql(mlb_postpitch, 'mlb_postpitching')
transfer_tosql(mlb_team, 'mlb_teams')

# Women Soccer
transfer_tosql(wsoc_goal, 'women_soccer_goals')
transfer_tosql(wsoc_teams, 'women_soccer_teams')
transfer_tosql(wsoc_franch, 'women_soccer_franchise')
transfer_tosql(wsoc_games_r, 'women_soccer_games')
transfer_tosql(wsoc_player, 'women_soccer_players')
transfer_tosql(wsoc_fieldplayer, 'women_soccer_fieldplayer')
transfer_tosql(wsoc_playfield, 'women_soccer_playfield')
transfer_tosql(wsoc_playstat, 'women_soccer_play_stats')
transfer_tosql(wsoc_stadium, 'women_soccer_stadium')

# College Ball
transfer_tosql(men_players, 'mncaa_players')
transfer_tosql(men_cities, 'mncaa_cities')
transfer_tosql(men_coaches, 'mncaa_coaches')
transfer_tosql(men_conference_games, 'mncaa_conference_games')
transfer_tosql(men_conference, 'mncaa_conference')
transfer_tosql(men_teamconference, 'mncaa_teamconference')
transfer_tosql(men_teams, 'mncaa_teams')
transfer_tosql(men_tournament, 'mncaa_tournament')
transfer_tosql(women_players, 'wncaa_players')
transfer_tosql(women_cities, 'wncaa_cities')
transfer_tosql(women_gamecities, 'wncaa_gamecities')
transfer_tosql(women_conference, 'wncaa_conference')
transfer_tosql(women_season, 'wncaa_season')
transfer_tosql(women_seasongames, 'wncaa_seasongames')
