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


def college_ball():
    client = Client(n_workers=100, threads_per_worker=55, processes=False, memory_limit='50GB')
    print(client)

    # Men College NCAA
    ncam_players = dd.read_csv(
        's3://sportsdatawarehouse/NCAAmen/men_ncaa_data/DataFiles/playbyplay/files/Players_*.csv').compute()
    ncam_cities = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_cities.csv').compute()
    ncam_coaches = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_coaches.csv').compute()
    ncam_conference = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_conference.csv').compute()
    ncam_conf_gmes = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_confgames.csv').compute()
    ncam_gamecities = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_gamecities.csv').compute()
    ncam_seasongames = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_season_games.csv').compute()
    ncam_teamconf = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tconf.csv').compute()
    ncam_teams = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_teams.csv').compute()
    ncam_tournament = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_tournament.csv').compute()

    ncam_players['league'] = 'NCAA'
    ncam_players['sport'] = 'Basketball'
    ncam_players['gender'] = 'Male'

    # Women College NCAA
    # ncaw_events = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/data/WEvents*.csv')
    ncaw_players = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/data/WPlayers.csv').compute()
    ncaw_cities = dd.read_csv('s3://sportsdatawarehouse/NCAAmen/men_ncaa_data/mncaa_cities.csv').compute()
    ncaw_conference = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_conference.csv').compute()
    ncaw_gamecities = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_gamecities.csv').compute()
    ncaw_seasongames = dd.read_csv(
        's3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_season_games.csv').compute()
    ncaw_season = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_seasons.csv').compute()
    ncaw_teamconf = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tconf.csv').compute()
    ncaw_teams = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_teams.csv').compute()
    ncaw_tournament = dd.read_csv('s3://sportsdatawarehouse/NCAAwomen/women_ncaa_data/wncaa_tournament.csv').compute()
    ncaw_players['league'] = 'NCAA'
    ncaw_players['sport'] = 'Basketball'
    ncaw_players['gender'] = 'Female'
    print(ncam_players.head())

    # Drop Missing Values
    men_players = ncam_players.dropna()
    men_cities = ncam_cities.dropna()
    men_coaches = ncam_coaches.dropna()
    men_conference = ncam_conference.dropna()
    men_conference_games = ncam_conf_gmes.dropna()
    men_gamecities = ncam_gamecities.dropna()
    men_teamconf = ncam_teamconf.dropna()
    men_teams = ncam_teams.dropna()
    men_tournaments = ncam_tournament.dropna()
    men_seasongames = ncam_seasongames.dropna()

    women_players = ncaw_players.dropna()
    women_cities = ncaw_cities.dropna()
    women_conference = ncaw_conference.dropna()
    women_gamecities = ncaw_gamecities.dropna()
    women_seasongames = ncaw_seasongames.dropna()
    women_season = ncaw_season.dropna()
    women_teamconf = ncaw_teamconf.dropna()
    women_teams = ncaw_teams.dropna()
    women_tournament = ncaw_tournament.dropna()

    # Transfer Data stored in Dask to Postgres SQL

    # Creating connection

    engine = sqlalchemy.create_engine('postgresql://' + config.username + ':' + config.password + '@' + config.endpoint)
    con = engine.connect()

    men_players.to_sql('mncaa_players', con=engine, if_exists='replace', index=False)
    men_cities.to_sql('mncaa_cities', con=engine, if_exists='replace', index=False)
    men_coaches.to_sql('mncaa_coaches', con=engine, if_exists='replace', index=False)
    men_conference.to_sql('mncaa_conference', con=engine, if_exists='replace', index=False)
    men_conference_games.to_sql('mncaa_conference_games', con=engine, if_exists='replace', index=False)
    men_gamecities.to_sql('mncaa_gamecities', con=engine, if_exists='replace', index=False)
    men_teamconf.to_sql('mncaa_teamconference', con=engine, if_exists='replace', index=False)
    men_teams.to_sql('mncaa_teams', con=engine, if_exists='replace', index=False)
    men_tournaments.to_sql('mncaa_tournament', con=engine, if_exists='replace', index=False)
    women_players.to_sql('wncaa_players', con=engine, if_exists='replace', index=False)
    men_seasongames.to_sql('mncaa_seasongames',con=engine, if_exists='replace', index=False)
    women_cities.to_sql('wncaa_cities', con=engine, if_exists='replace', index=False)
    women_conference.to_sql('wncaa_conference', con=engine, if_exists='replace', index=False)
    women_gamecities.to_sql('wncaa_gamecities', con=engine, if_exists='replace', index=False)
    women_seasongames.to_sql('wncaa_seasongames', con=engine, if_exists='replace', index=False)
    women_season.to_sql('wncaa_season', con=engine, if_exists='replace', index=False)
    women_teamconf.to_sql('wncaa_teamconference', con=engine, if_exists='replace', index=False)
    women_tournament.to_sql('wncaa_tournament', con=engine, if_exists='replace', index=False)


if __name__ == "__main__":
    college_ball()
