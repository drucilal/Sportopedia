import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os

def football():
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
    nba_game_details = dd.read_csv('s3://sportsdatawarehouse/NBA/games_details.csv').compute()

    # Drop Missing Values
    afc_rec = afc.dropna()
    afl_rec = afl.dropna()
    d_game_stat = defense_game_stat.dropna()
    d_intecep = defense_intecep.dropna()
    d_pass = defense_pass.dropna()
    d_receive = defense_rece.dropna()
    defense_r = defense_rush.dropna()
    defense_s = defense_score.dropna()
    d_tackle = defense_tackle.dropna()
    nfc_rec = nfc.dropna()
    nfl_rec = nfl_records.dropna()
    o_field = offense_field.dropna()
    o_game = offense_game_stat.dropna()
    o_k = offense_kicking.dropna()
    off_kickreturn = offense_kick_return.dropna()
    off_line = offense_offensive_line.dropna()
    of_pass = offence_pass.dropna()
    of_pun = offense_pun.dropna()
    of_rece = offense_rece.dropna()
    off_rush = offense_rush.dropna()
    off_score = offense_score.dropna()
    off_touch = offense_touch.dropna()
    merg_data = merged.dropna()
    superb = superbowl.dropna()
    nba_game_d = nba_game_details.dropna()
    # Transfer Data to PostGres

    engine = sqlalchemy.create_engine('postgresql://' + config.username + ':' + config.password + '@' + config.endpoint)
    con = engine.connect()


    afc_rec.to_sql('afc_records', con=engine, if_exists='replace', index=False)
    afl_rec.to_sql('afl_records', con=engine, if_exists='replace', index=False)
    d_game_stat.to_sql('defense_gamestatistics', con=engine, if_exists='replace', index=False)
    d_intecep.to_sql('defense_interception', con=engine, if_exists='replace', index=False)
    d_pass.to_sql('defense_pass', con=engine, if_exists='replace', index=False)
    d_receive.to_sql('defense_receive', con=engine, if_exists='replace', index=False)
    defense_r.to_sql('defense_rush', con=engine, if_exists='replace', index=False)
    defense_s.to_sql('defense_score', con=engine, if_exists='replace', index=False)
    d_tackle.to_sql('defense_tackle', con=engine, if_exists='replace', index=False)
    nfc_rec.to_sql('nfc_records', con=engine, if_exists='replace', index=False)
    nfl_rec.to_sql('nfl_records', con=engine, if_exists='replace', index=False)
    o_field.to_sql('offense_fieldgoals', con=engine, if_exists='replace', index=False)
    o_game.to_sql('offense_game_stats', con=engine, if_exists='replace', index=False)
    o_k.to_sql('offense_kicks', con=engine, if_exists='replace', index=False)
    off_kickreturn.to_sql('offense_kickreturns', con=engine, if_exists='replace', index=False)
    off_line.to_sql('offense_line', con=engine, if_exists='replace', index=False)
    of_pass.to_sql('offense_passing', con=engine, if_exists='replace', index=False)
    of_pun.to_sql('offense_punting', con=engine, if_exists='replace', index=False)
    of_rece.to_sql('offense_receiving', con=engine, if_exists='replace', index=False)
    off_rush.to_sql('offense_rushing', con=engine, if_exists='replace', index=False)
    off_score.to_sql('offense_score', con=engine, if_exists='replace', index=False)
    off_touch.to_sql('offense_touch', con=engine, if_exists='replace', index=False)
    merg_data.to_sql('offense_defense', con=engine, if_exists='replace', index=False)
    superb.to_sql('superbowl', con=engine, if_exists='replace', index=False)
    nba_game_d.to_sql('nba_game_details', con=engine, if_exists='replace', index=False)

    con.close()


if __name__ == "__main__":
    football()
