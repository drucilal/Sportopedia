import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
from dask.distributed import Client


def baseball():
    client = Client(n_workers=100, threads_per_worker=55, processes=False, memory_limit='50GB')
    print(client)

    # MLB Baseball Data Sources

    mlb_allstar = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AllstarFull.csv').compute()
    mlb_appearances = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Appearances.csv',
                                  dtype={'G_dh': 'float64'}).compute()
    mlb_awardmanagers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsManagers.csv').compute()
    mlb_awardplayers = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsShareManagers.csv').compute()
    mlb_awardshared_players = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/AwardsSharePlayers.csv').compute()
    mlb_batting = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Batting.csv').compute()
    mlb_postbatting = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/BattingPost.csv').compute()
    mlb_college = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/CollegePlaying.csv').compute()
    mlb_fielding = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Fielding.csv', dtype={'E': 'float64',
                                                                                             'InnOuts': 'float64'}).compute()
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
    wsocer_player = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_player.csv').compute()
    wsoccer_playfield = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_playfield.csv').compute()
    wsoccer_playstats = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccer_playstats.csv').compute()
    wsoccer_franch = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccerfranchises.csv').compute()
    wsoccer_games_r = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccergameresults.csv').compute()
    wsoccer_teams = dd.read_csv('s3://sportsdatawarehouse/women_soccer/wsoccerteam_stats.csv').compute()

    # Transforming
    fill_star = {'startingPos': 0.0}
    mlb_allstar = mlb_allstar.fillna(fill_star)
    mlb_allstar = mlb_allstar.dropna(subset=['yearID'])
    mlb_allstar = mlb_allstar.dropna(subset=['gameNum'])
    mlb_allstar = mlb_allstar.dropna(subset=['gameID'])
    fill2 = {'lgID': 'n', 'GS': 0.0, 'G_defense': 0.0, 'G_dh': 0.0, 'G_ph': 0.0, 'G_pr': 0.0}
    mlb_appearances = mlb_appearances.fillna(fill2)
    mlb_awardmanagers = mlb_awardmanagers.fillna({'tie': 'none', 'notes': 'none'})
    mlb_awardplayers = mlb_awardplayers.fillna({'pointsMax': 0.0})
    mlb_awardshared_players = mlb_awardshared_players.fillna({'votesFirst': 0.0})
    mlb_batting = mlb_batting.fillna({'lgID': 'n', 'RBI': 0.0, 'SB': 0.0, 'CS': 0.0, 'SO': 0.0,
                                      'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0, 'SF': 0.0, 'GIDP': 0.0})
    mlb_postbatting = mlb_postbatting.fillna({'CS': 0.0, 'HBP': 0.0, 'SH': 0.0, 'SF': 0.0, 'GIDP': 0.0})
    mlb_fielding = mlb_fielding.fillna({'lgID': 'n', 'GS': 0.0, 'InnOuts': 0.0, 'PB': 0.0, 'WP': 0.0, 'SB': 0.0,
                                        'CS': 0.0, 'ZR': 0.0})
    mlb_fieldingof = mlb_fieldingof.fillna({'Glf': 0.0, 'Gcf': 0.0, 'Grf': 0.0})
    mlb_fieldingpost = mlb_fieldingpost.fillna({'PB': 0.0, 'SB': 0.0, 'CS': 0.0})

    mlb_halloffame = mlb_halloffame.fillna({'ballots': 0.0, 'needed': 0.0, 'votes': 0.0, 'needed_note': 'none'})

    mlb_homegames = mlb_homegames.fillna({'league.key': 'n'})

    mlb_managers = mlb_managers.fillna({'lgID': 'n', 'plyrMgr': 'N'})
    mlb_parks = mlb_parks.fillna({'park.alias': 'none', 'country': 'n'})
    mlb_players = mlb_players.fillna({'birthYear': 0.0, 'birthMonth': 0.0, 'birthDay': 0.0, 'birthCountry': 'none',
                                      'birthState': 'none', 'birthCity': 'none', 'deathYear': 0.0, 'deathMonth': 0.0,
                                      'deathCountry': 'none', 'deathState': 'none', 'deathCity': 'none',
                                      'nameFirst': 'unknown', 'nameGiven': 'unknown', 'weight': 0.0, 'height': 0.0,
                                      'bats': 'n', 'throws': 'n'})
    mlb_players = mlb_players.dropna(subset=['debut', 'finalGame', 'retroID', 'bbrefID'])
    mlb_pitching = mlb_pitching.fillna({'lgID': 'n', 'BAOpp': 0.0, 'ERA': 0.0, 'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0,
                                        'SF': 0.0, 'GIDP': 0.0})
    mlb_postpitching = mlb_postpitching.fillna(
        {'WP': 0.0, 'BK': 0.0, 'BFP': 0.0, 'BAOpp': 0.0, 'ERA': 0.0, 'IBB': 0.0, 'HBP': 0.0, 'SH': 0.0,
         'SF': 0.0, 'GIDP': 0.0})
    mlb_teams = mlb_teams.fillna(
        {'lgID': 'n', 'divID': 'n', 'Ghome': 0.0, 'DivWin': 'n', 'WCWin': 'n', 'LgWin': 'n', 'WSWin': 'n',
         'BB': 0.0, 'SO': 0.0, 'SB': 0.0, 'CS': 0.0, 'HBP': 0.0, 'SF': 0.0, 'park': 'n', 'attendance': 0.0})
    mlb_teams['league'] = 'MLB'
    mlb_teams['sport'] = 'baseball'
    mlb_teams['gender'] = 'male'
    mlb_teams_franch = mlb_teams_franch.fillna({'active': 'm', 'NAassoc': 'none'})

    wsoccer_stadium = wsoccer_stadium.dropna(subset=['pri_stadium_alias', 'sec_stadium_name', 'sec_stadium_alias',
                                                     'sec_town', 'sec_state', 'sec_capacity'])
    wsoccer_fieldplayer = wsoccer_fieldplayer.fillna({'nation': 'n', 'min': 0.0, 'pk': 0.0, 'p_katt': 0.0})
    wsoccer_goal = wsoccer_goal.fillna({'nation': 'n', 'so_ta': 0.0, 'saves': 0.0, 'saves_pct': 60,
                                        'crd_y': 0.0, 'crd_r': 57})
    wsocer_player = wsocer_player.dropna(subset=['name_other'])
    wsocer_player = wsocer_player.fillna({'nation': 'n'})
    wsoccer_games_r = wsoccer_games_r.fillna({'winner': 'unknown'})
    wsoccer_teams['league'] = 'NWSL'
    wsoccer_teams['sport'] = 'soccer'
    wsoccer_teams['gender'] = 'female'
    wsoccer_teams = wsoccer_teams.dropna()


    # Transfer Data stored in Dask to Postgres SQL

    # Creating connection

    engine = sqlalchemy.create_engine('postgresql://' + config.username + ':' + config.password + '@' + config.endpoint)
    con = engine.connect()

    mlb_allstar.to_sql('mlb_allstar_games', con=engine, if_exists='replace', index=False)
    mlb_appearances.to_sql('mlb_appearances', con=engine, if_exists='replace', index=False)
    mlb_awardmanagers.to_sql('mlb_award_managers', con=engine, if_exists='replace', index=False)
    mlb_awardplayers.to_sql('mlb_award_players', con=engine, if_exists='replace', index=False)
    mlb_awardshared_players.to_sql('mlb_awardshared_players', con=engine, if_exists='replace', index=False)
    mlb_batting.to_sql('mlb_batting', con=engine, if_exists='replace', index=False)
    mlb_postbatting.to_sql('mlb_postbatting', con=engine, if_exists='replace', index=False)
    mlb_fielding.to_sql('mlb_fielding', con=engine, if_exists='replace', index=False)
    mlb_fieldingof.to_sql('mlb_fieldingof', con=engine, if_exists='replace', index=False)
    mlb_fieldingpost.to_sql('mlb_fieldingpost', con=engine, if_exists='replace', index=False)
    mlb_halloffame.to_sql('mlb_halloffame', con=engine, if_exists='replace', index=False)
    mlb_homegames.to_sql('mlb_homegames', con=engine, if_exists='replace', index=False)
    mlb_managers.to_sql('mlb_managers', con=engine, if_exists='replace', index=False)
    mlb_parks.to_sql('mlb_parks', con=engine, if_exists='replace', index=False)
    mlb_players.to_sql('mlb_players', con=engine, if_exists='replace', index=False)
    mlb_teams.to_sql('mlb_teams', con=engine, if_exists='replace', index=False)
    wsoccer_stadium.to_sql('women_soccer_stadium', con=engine, if_exists='replace', index=False)
    wsoccer_fieldplayer.to_sql('women_soccer_fieldplayer', con=engine, if_exists='replace', index=False)
    wsoccer_goal.to_sql('women_soccer_goals', con=engine, if_exists='replace', index=False)
    wsocer_player.to_sql('women_player_', con=engine, if_exists='replace', index=False)
    wsoccer_games_r.to_sql('wommen_soccer_games', con=engine, if_exists='replace', index=False)
    wsoccer_teams.to_sql('women_soccer_teams', con=engine, if_exists='replace', index=False)

    con.close()

if __name__ == "__main__":
    baseball()
