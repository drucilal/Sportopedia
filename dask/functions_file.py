import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os

def read_files(file):
    """
    Function to read in files into dask cluster 
    data = dask dataframe variable
    """
    data = dd.read_csv(file).compute()
    return data

def read_files_datatypes(filename,dtype):
    data = dd.read_csv(filename,dtype).compute()
    return data

def merge_columns(df1,df2,cols):
    """
    Function to merge datasets into one based on their common column
    df1 = first dataframe
    df2 = second dataframe
    cols = column or columns to merge on
    we want to check and remove the Unnamed:0 column
    """
    data = dd.merge(df1,df2,on=cols)
    if 'Unnamed: 0' in data:
            data = data.drop('Unnamed: 0', axis=1)
    return data

def add_unique_ids(df):
    """
    Merge data files by id columns 
    player id and team id
    player_data = dataframe that consist of just the player id merged
    data = consist of team id and player id
    """
    player_data = merge_columns(df,mlb_players_ids,'playerID')
    data = merge_columns(player_data,mlb_teams_id,'teamID')
    return data

def remove_percent_signs(df):
    """
    Remove percent signs and replace with abbrev:pct
    """
    df.columns = df.columns.str.replace('%', 'pct')
    df = df.fillna(0.0)
    return df

def drop_values(df):
    """
    Drop the rest of the missing values
    """
    data = df.dropna()
    return data

def transfer_tosql(df,table_name):
    """
    Transfer selected dataframe to Postgresql
    Create a connection
    df = datafarme 
    table_name = chosen table name
    """
    engine = sqlalchemy.create_engine()
    con = engine.connect()
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    return con.close()

