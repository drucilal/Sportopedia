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

from dask.distributed import Client

def basketball_one():
    client = Client(n_workers=100, threads_per_worker=55, processes=False, memory_limit='50GB')
    print(client)
    # NBA
    nba_t = 's3://sportsdatawarehouse/NBA/teams/NBA_teams_team stats_*.csv'
    nba_p = 's3://sportsdatawarehouse/NBA/players/NBA_Players_per game stats_*.csv'
    nba_op = 's3://sportsdatawarehouse/NBA/opponents/NBA_teams_opp stats_*.csv'
    nba_sa = 's3://sportsdatawarehouse/NBA/salary/*nbasalary.csv'

    # WNBA
    wnba_t = 's3://sportsdatawarehouse/WNBA/team/wbna_team*.csv'
    wnba_p = 's3://sportsdatawarehouse/WNBA/players/wbna_player*.csv'
    wnba_sa = 's3://sportsdatawarehouse/WNBA/salaries/*_team_salaries.csv'

    # Key Identifiers
    nba_team_ids = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/nba_team.csv')
    nba_player_ids = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/nba_players.csv')
    wnba_team_ids = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/wnba_team.csv')
    wnba_player_ids = dd.read_csv('s3://sportsdatawarehouse/key_identifiers/wnba_players.csv')

    nba_team_id = nba_team_ids.compute()
    nba_player_id = nba_player_ids.compute()
    wnba_team_id = wnba_team_ids.compute()
    wnba_player_id = wnba_player_ids.compute()
    nba_teams = dd.read_csv(nba_t).compute()
    nba_players = dd.read_csv(nba_p).compute()
    nba_opponents = dd.read_csv(nba_op).compute()
    nba_salaries = dd.read_csv(nba_sa).compute()
    wnba_team = dd.read_csv(wnba_t).compute()
    wnba_player = dd.read_csv(wnba_p).compute()
    wnba_salary = dd.read_csv(wnba_sa).compute()
    fill_teams = {'3P': 0.0, '3PA': 0.0, '3P%': 0.0}
    fill_players = {'GS': 0.0, 'FG%': 0.0, '3P': 0.0, '3PA': 0.0, '3P%': 0.0, '2PA': 0.0,
                    '2P%': 0.0, 'eFG%': 0.0, 'FT': 0.0, 'FT%': 0.0, 'TOV': 0.0}
    rename_cols = {'FG%': 'FG_pct', '3P%': '3P_pct', 'eFG%': 'eFG_pct', '2P%': '2P_pct', 'FT%': 'FT_pct'}
    nba_team = nba_teams.drop('Unnamed: 0', axis=1)
    nba_players = nba_players.drop('Unnamed: 0', axis=1)
    nba_play = nba_players.dropna(subset=['Player'])
    nba_opponent = nba_opponents.drop('Unnamed: 0', axis=1)
    nba_salary = nba_salaries.drop('Unnamed: 0', axis=1)
    nba_teams_df = nba_team.fillna(fill_teams)
    nba_teams_df = nba_teams.rename(columns=rename_cols)
    nba_teams_df['league'] = 'NBA'
    nba_teams_df['sport'] = 'Basketball'
    nba_teams_df['gender'] = 'male'
    nba_players_df = nba_play.fillna(fill_players)
    nba_players_df = nba_players_df.rename(columns=rename_cols)
    nba_salary_df = nba_salary[['Name', 'Team', 'Salary']]
    wnba_team['Western Conference'] = wnba_team['Western Conference'].str.replace('*', '')
    rename_team = {'Western Conference': 'team'}
    rename_cols = {'FG%': 'FG_pct', '3P%': '3P_pct', 'eFG%': 'eFG_pct', '2P%': '2P_pct', 'FT%': 'FT_pct'}
    fill_players = {'Pos': 'N', 'FG%': 0.0, '3P%': 0.0, '2P%': 0.0, 'eFG%': 0.0, 'FT%': 0.0}
    wnba_team = wnba_team.rename(columns=rename_team)
    wnba_team = wnba_team.rename(columns=rename_cols)
    wnba_team['league'] = 'WNBA'
    wnba_team['sport'] = 'Basketball'
    wnba_team['gender'] = 'female'
    wnba_player = wnba_player.rename(columns=rename_cols)
    wnba_player = wnba_player.fillna(fill_players)
    wnba_salary = wnba_salary[['index', 'Team', 'Average Age', 'Active Cap', 'season']]
    wnba_salary['Active Cap'] = wnba_salary['Active Cap'].str.replace(',', '').str.replace('$', '').astype(int)
    fill_star = {'startingPos': 0.0}

    nba_team_rf = nba_teams_df.drop(['Unnamed: 0'], axis=1)
    wnba_teamr = wnba_team.drop(['Rk'], axis=1)

    # Melt Dataframe
    nba_team_reshaped = nba_team_rf.melt(id_vars=['Team', 'season', 'league', 'sport', 'gender'],
                                         var_name='statistic_name', value_name='statistic')
    nba_players_reshaped = nba_players_df.melt(id_vars=['Player', 'Pos', 'Age', 'Tm', 'season'],
                                               var_name='statistic_name', value_name='statistic')
    wnba_team_reshaped = wnba_teamr.melt(id_vars=['team', 'season', 'league', 'sport', 'gender'],
                                         var_name='statistic_name', value_name='statistic')
    wnba_player_reshaped = wnba_player.melt(id_vars=['Player', 'Tm', 'Pos', 'season'],
                                            var_name='statistic_name', value_name='statistic')


    con = engine.connect()
    nba_team_reshaped.to_sql('nba_teams', con=engine, if_exists='replace', index=False)
    nba_team_id.to_sql('nba_team_list', con=engine, if_exists='replace', index=False)

    nba_player_id.to_sql('nba_player_list', con=engine, if_exists='replace', index=False)
    nba_players_df.to_sql('nba_players_norm', con=engine, if_exists='replace', index=False)
    nba_players_reshaped.to_sql('nba_players', con=engine, if_exists='replace', index=False)
    nba_salary_df.to_sql('nba_salary', con=engine, if_exists='replace', index=False)
    wnba_team_reshaped.to_sql('wnba_teams', con=engine, if_exists='replace', index=False)
    wnba_player_reshaped.to_sql('wnba_players', con=engine, if_exists='replace', index=False)
    wnba_team_id.to_sql('wnba_team_list', con=engine, if_exists='replace', index=False)
    wnba_player_id.to_sql('wnba_players_list', con=engine, if_exists='replace', index=False)
    wnba_salary.to_sql('wnba_salary', con=engine, if_exists='replace', index=False)

    con.close()


if __name__ == "__main__":
    basketball_one()

