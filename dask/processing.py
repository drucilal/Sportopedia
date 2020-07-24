import pylint
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

# NBA

# Merge players and teams dataset togehter
players = merge_columns(nba_player_info,nba_player,'Player')
players_teams = merge_columns(players,nba_teamid,'Tm')
player_teams_s = merge_columns(players_teams,nba_salary,['Player','Team','season'])
# Remove percentage sign
nba_full_team = remove_percent_signs(player_teams_s)
print(nba_full_team.columns)
# WNBA
wnba_team.rename(columns={'Western Conference': 'Team'}, inplace=True)
wnba_team_info = merge_columns(wnba_team,wnba_salary,['Team','season'])
wnba_players_info = merge_columns(wnba_teamid,wnba_player,'Tm')
wnba_team_details = remove_percent_signs(wnba_team_info)
wnba_players_info = remove_percent_signs(wnba_players_info)

# Extract Players IDs
mlb_players_ids = mlb_players[['playerID','nameFirst','nameLast']]
mlb_teams_id = mlb_teams[['teamID','name']]
# MLB
# MLB Players
mlb_players_info = merge_columns(mlb_players,mlb_salaries,'playerID')
mlb_player_school_info = merge_columns(mlb_players_info,mlb_college,'playerID')
mlb_player_details = merge_columns(mlb_player_school_info,mlb_schools,'schoolID')

# MLB Stadium 
mlb_stadiums = merge_columns(mlb_homegames,mlb_parks,'park.key')


mlb_batting_details  = add_unique_ids(mlb_batting,mlb_players_ids,mlb_teams_id)
mlb_pitching_details = add_unique_ids(mlb_pitching,mlb_players_ids,mlb_teams_id)
mlb_fielding_details = add_unique_ids(mlb_fielding,mlb_players_ids,mlb_teams_id)
mlb_allstar_details = add_unique_ids(mlb_allstars,mlb_players_ids,mlb_teams_id)
mlb_halloffame_details = merge_columns(mlb_halloffame,mlb_players_ids,'playerID')


# NFL: Superbowl files and Regular Seasons

# College Men Basketball 
ncam_team_details = merge_columns(ncam_teams,ncam_coaches,'team_id')
ncam_conference_i = merge_columns(ncam_conference,ncam_conference_games,'conf_abbrev')
ncam_conference_info = merge_columns(ncam_conference_i,ncam_conference,'conf_abbrev')
ncam_gamecities_info = merge_columns(ncam_cities,ncam_gamecities,'city_id')

# College Women Basketball
ncaw_team_details = merge_columns(ncaw_teams,ncaw_teamconference,'team_id')

# Soccer
mls_players_1997_1 = merge_columns(mls_assist_1997,mls_fouls_1997,['Player','Club','POS','GP','GS','A'])
mls_players_1997 = merge_columns(mls_players_1997_1,mls_shots_1997,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_1997['Season'] = '1997'
mls_players_1998_1 = merge_columns(mls_assist_1998,mls_fouls_1998,['Player','Club','POS','GP','GS','A'])
mls_players_1998 = merge_columns(mls_players_1998_1,mls_shots_1998,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_1998['Season'] = '1998'
mls_players_1999_1 = merge_columns(mls_assist_1999,mls_fouls_1999,['Player','Club','POS','GP','GS','A'])
mls_players_1999 = merge_columns(mls_players_1999_1,mls_shots_1999,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_1999['Season'] = '1999'

mls_players_2000_1 = merge_columns(mls_assist_2000,mls_fouls_2000,['Player','Club','POS','GP','GS','A'])
mls_players_2000 = merge_columns(mls_players_2000_1,mls_shots_2000,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2000['Season'] = '2000'

mls_players_2001_1 = merge_columns(mls_assist_2001,mls_fouls_2001,['Player','Club','POS','GP','GS','A'])
mls_players_2001 = merge_columns(mls_players_2001_1,mls_shots_2001,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2001['Season'] = '2001'
mls_players_2002_1 = merge_columns(mls_assist_2002,mls_fouls_2002,['Player','Club','POS','GP','GS','A'])
mls_players_2002 = merge_columns(mls_players_2002_1,mls_shots_2002,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2002['Season'] = '2002'
mls_players_2003_1 = merge_columns(mls_assist_2003,mls_fouls_2003,['Player','Club','POS','GP','GS','A'])
mls_players_2003 = merge_columns(mls_players_2003_1,mls_shots_2003,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2003['Season'] = '2003'
mls_players_2004_1 = merge_columns(mls_assist_2004,mls_fouls_2004,['Player','Club','POS','GP','GS','A'])
mls_players_2004 = merge_columns(mls_players_2004_1,mls_shots_2004,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2004['Season'] = '2004'
mls_players_2005_1 = merge_columns(mls_assist_2005,mls_fouls_2005,['Player','Club','POS','GP','GS','A'])
mls_players_2005 = merge_columns(mls_players_2005_1,mls_shots_2005,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2005['Season'] = '2005'
mls_players_2006_1 = merge_columns(mls_assist_2006,mls_fouls_2006,['Player','Club','POS','GP','GS','A'])
mls_players_2006 = merge_columns(mls_players_2006_1,mls_shots_2006,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2006['Season'] = '2006'
mls_players_2007_1 = merge_columns(mls_assist_2007,mls_fouls_2007,['Player','Club','POS','GP','GS','A'])
mls_players_2007 = merge_columns(mls_players_2007_1,mls_shots_2007,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2007['Season'] = '2007'
mls_players_2008_1 = merge_columns(mls_assist_2008,mls_fouls_2008,['Player','Club','POS','GP','GS','A'])
mls_players_2008 = merge_columns(mls_players_2008_1,mls_shots_2008,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2008['Season'] = '2008'
mls_players_2009_1 = merge_columns(mls_assist_2009,mls_fouls_2009,['Player','Club','POS','GP','GS','A'])
mls_players_2009 = merge_columns(mls_players_2009_1,mls_shots_2009,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2009['Season'] = '2009'
mls_players_2010_1 = merge_columns(mls_assist_2010,mls_fouls_2010,['Player','Club','POS','GP','GS','A'])
mls_players_2010 = merge_columns(mls_players_2010_1,mls_shots_2010,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2010['Season'] = '2010'
mls_players_2011_1 = merge_columns(mls_assist_2011,mls_fouls_2011,['Player','Club','POS','GP','GS','A'])
mls_players_2011 = merge_columns(mls_players_2011_1,mls_shots_2011,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2011['Season'] = '2011'
mls_players_2012_1 = merge_columns(mls_assist_2012,mls_fouls_2012,['Player','Club','POS','GP','GS','A'])
mls_players_2012 = merge_columns(mls_players_2012_1,mls_shots_2012,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2012['Season'] = '2012'
mls_players_2013_1 = merge_columns(mls_assist_2013,mls_fouls_2013,['Player','Club','POS','GP','GS','A'])
mls_players_2013 = merge_columns(mls_players_2013_1,mls_shots_2013,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2013['Season'] = '2013'
mls_players_2014_1 = merge_columns(mls_assist_2014,mls_fouls_2014,['Player','Club','POS','GP','GS','A'])
mls_players_2014 = merge_columns(mls_players_2014_1,mls_shots_2014,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2014['Season'] = '2014'
mls_players_2015_1 = merge_columns(mls_assist_2015,mls_fouls_2015,['Player','Club','POS','GP','GS','A'])
mls_players_2015 = merge_columns(mls_players_2015_1,mls_shots_2015,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2015['Season'] = '2015'
mls_players_2016_1 = merge_columns(mls_assist_2016,mls_fouls_2016,['Player','Club','POS','GP','GS','A'])
mls_players_2016 = merge_columns(mls_players_2016_1,mls_shots_2016,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2016['Season'] = '2016'
mls_players_2017_1 = merge_columns(mls_assist_2017,mls_fouls_2017,['Player','Club','POS','GP','GS','A'])
mls_players_2017 = merge_columns(mls_players_2017_1,mls_shots_2017,['Player','Club','POS','GP','A','G','GS','MINS','SHTS','SOG'])
mls_players_2017['Season'] = '2017'



mls_teams_1997['Season'] = '1997'
mls_teams_1998['Season'] = '1998'
mls_teams_1999['Season'] = '1999'
mls_teams_2000['Season'] = '2000'
mls_teams_2001['Season'] = '2001'
mls_teams_2002['Season'] = '2002'
mls_teams_2003['Season'] = '2003'
mls_teams_2004['Season'] = '2004'
mls_teams_2005['Season'] = '2005'
mls_teams_2006['Season'] = '2006'
mls_teams_2007['Season'] = '2007'

mls_teams_2008['Season'] = '2008'
mls_teams_2009['Season'] = '2009'
mls_teams_2010['Season'] = '2010'
mls_teams_2011['Season'] = '2011'
mls_teams_2012['Season'] = '2012'
mls_teams_2013['Season'] = '2013'
mls_teams_2014['Season'] = '2014'
mls_teams_2015['Season'] = '2015'
mls_teams_2016['Season'] = '2016'
mls_teams_2017['Season'] = '2017'

mls_teams = pd.concat([mls_teams_1997,mls_teams_1998,mls_teams_1999,mls_teams_2000,mls_teams_2001,mls_teams_2002,
mls_teams_2003,mls_teams_2004,mls_teams_2005,mls_teams_2006,mls_teams_2007,mls_teams_2008,mls_teams_2009,mls_teams_2010,
mls_teams_2011,mls_teams_2012,mls_teams_2013,mls_teams_2014,mls_teams_2015,mls_teams_2016,mls_teams_2017],axis=0)



mls_players = pd.concat([mls_players_1997,mls_players_1998,mls_players_1999,mls_players_2000,mls_players_2001,mls_players_2002,
mls_players_2003,mls_players_2004,mls_players_2005,mls_players_2006,mls_players_2007,mls_players_2008,mls_players_2009,mls_players_2010,
mls_players_2011,mls_players_2012,mls_players_2013,mls_players_2014,mls_players_2015,mls_players_2016,mls_players_2017],axis =0)

mls_players = remove_percent_signs(mls_players)



player = mls_players.Player.unique()
player_id = np.random.randint(100,size=(2671))

player_series = pd.Series(player)
playerid_series = pd.Series(player_id)

frame = {'Player':player_series,'Player_id': playerid_series}
result = pd.DataFrame(frame)
mls_final_players = merge_columns(result,mls_players,'Player')


