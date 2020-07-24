import pandas as pd
import dask.dataframe as dd
import numpy as np
import boto3
import s3fs
import os
import functions_file
from functions_file import *


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
wnba_teamid =  read_files('s3://sportsdatawarehouse/key_identifiers/wnba_teamID.csv')
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
mlb_teams = dd.read_csv('s3://sportsdatawarehouse/MLB/mlb_teams.csv',dtype={'DivWin': 'object',
       'WCWin': 'object',
       'divID': 'object'}).compute()
mlb_appearances = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Appearances.csv',
                              dtype={'G_dh': 'float64'}).compute()
mlb_fielding = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Fielding.csv',
                           dtype={'E': 'float64', 'InnOuts': 'float64'}).compute()

mlb_pitching = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Pitching.csv',
                           dtype={'BFP': 'float64'}).compute()

mlb_teams = dd.read_csv('s3://sportsdatawarehouse/MLB/2019/core/Teams.csv', dtype={'DivWin': 'object',
                                                                                   'WCWin': 'object',
                                                                                   'divID': 'object'}).compute()

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
mlb_schools = read_files ('s3://sportsdatawarehouse/MLB/2019/core/Schools.csv')
mlb_teams_franch = read_files('s3://sportsdatawarehouse/MLB/2019/core/TeamsFranchises.csv')
mlb_halfteams = read_files('s3://sportsdatawarehouse/MLB/2019/core/TeamsHalf.csv')

# NFL Data
nfl = dd.read_csv('s3://sportsdatawarehouse/NFL_f/clean_offense_def.csv',
                     dtype={'Defense_passing_1stpct': 'float64',
                            'Defense_rushing_1stpct': 'float64',
                            'Offense_kicking_Avg': 'float64',
                            'Offense_kicking_Pct': 'float64',
                            'Offense_kicking_returns_Avg': 'float64',
                            'Offense_passing_1stpct': 'float64',
                            'Offense_punting_Net_Avg': 'float64',
                            'Offense_rushing_1stpct': 'float64'}).compute()
superbowl = read_files('s3://sportsdatawarehouse/NFL_f/Superbowl_winners.CSV')

# MLS Soccer

# 1997
mls_assist_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/assists.csv')
mls_fouls_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/fouls.csv')
mls_goal_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/goalkeeping.csv')
mls_saves_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/saves.csv')
mls_shots_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/shots.csv')
mls_shutouts_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/shutouts.csv')
mls_teams_1997 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1997/Teams/*.csv')

# 1998

mls_assist_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/assists.csv')
mls_fouls_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/fouls.csv')
mls_goal_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/goalkeeping.csv')
mls_saves_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/saves.csv')
mls_shots_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/shots.csv')
mls_shutouts_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/shutouts.csv')
mls_teams_1998 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1998/Teams/*.csv')

# 1999
mls_assist_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/assists.csv')
mls_fouls_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/fouls.csv')
mls_goal_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/goalkeeping.csv')
mls_saves_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/saves.csv')
mls_shots_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/shots.csv')
mls_shutouts_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/shutouts.csv')
mls_teams_1999 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/1999/Teams/*.csv')

# 2000
mls_assist_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/assists.csv')
mls_fouls_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/fouls.csv')
mls_goal_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/goalkeeping.csv')
mls_saves_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/saves.csv')
mls_shots_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/shots.csv')
mls_shutouts_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/shutouts.csv')
mls_teams_2000 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2000/Teams/*.csv')

# 2001
mls_assist_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/assists.csv')
mls_fouls_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/fouls.csv')
mls_goal_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/goalkeeping.csv')
mls_saves_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/saves.csv')
mls_shots_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/shots.csv')
mls_shutouts_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/shutouts.csv')
mls_teams_2001 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2001/Teams/*.csv')

# 2002
mls_assist_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/assists.csv')
mls_fouls_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/fouls.csv')
mls_goal_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/goalkeeping.csv')
mls_saves_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/saves.csv')
mls_shots_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/shots.csv')
mls_shutouts_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/shutouts.csv')
mls_teams_2002 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2002/Teams/*.csv')

#2003
mls_assist_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/assists.csv')
mls_fouls_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/fouls.csv')
mls_goal_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/goalkeeping.csv')
mls_saves_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/saves.csv')
mls_shots_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/shots.csv')
mls_shutouts_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/shutouts.csv')
mls_teams_2003 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2003/Teams/*.csv')

#2004
mls_assist_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/assists.csv')
mls_fouls_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/fouls.csv')
mls_goal_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/goalkeeping.csv')
mls_saves_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/saves.csv')
mls_shots_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/shots.csv')
mls_shutouts_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/shutouts.csv')
mls_teams_2004 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2004/Teams/*.csv')

# 2005
mls_assist_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/assists.csv')
mls_fouls_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/fouls.csv')
mls_goal_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/goalkeeping.csv')
mls_saves_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/saves.csv')
mls_shots_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/shots.csv')
mls_shutouts_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/shutouts.csv')
mls_teams_2005 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2005/Teams/*.csv')

# 2006
mls_assist_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/assists.csv')
mls_fouls_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/fouls.csv')
mls_goal_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/goalkeeping.csv')
mls_saves_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/saves.csv')
mls_shots_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/shots.csv')
mls_shutouts_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/shutouts.csv')
mls_teams_2006 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2006/Teams/*.csv')

#2007

mls_assist_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/assists.csv')
mls_fouls_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/fouls.csv')
mls_goal_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/goalkeeping.csv')
mls_saves_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/saves.csv')
mls_shots_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/shots.csv')
mls_shutouts_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/shutouts.csv')
mls_teams_2007 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2007/Teams/*.csv')

# 2008
mls_assist_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/assists.csv')
mls_fouls_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/fouls.csv')
mls_goal_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/goalkeeping.csv')
mls_saves_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/saves.csv')
mls_shots_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/shots.csv')
mls_shutouts_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/shutouts.csv')
mls_teams_2008 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2008/Teams/*.csv')

# 2009 
mls_assist_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/assists.csv')
mls_fouls_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/fouls.csv')
mls_goal_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/goalkeeping.csv')
mls_saves_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/saves.csv')
mls_shots_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/shots.csv')
mls_shutouts_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/shutouts.csv')
mls_teams_2009 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2009/Teams/*.csv')


# 2010 
mls_assist_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/assists.csv')
mls_fouls_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/fouls.csv')
mls_goal_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/goalkeeping.csv')
mls_saves_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/saves.csv')
mls_shots_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/shots.csv')
mls_shutouts_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/shutouts.csv')
mls_teams_2010 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2010/Teams/*.csv')

# 2011
mls_assist_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/assists.csv')
mls_fouls_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/fouls.csv')
mls_goal_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/goalkeeping.csv')
mls_saves_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/saves.csv')
mls_shots_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/shots.csv')
mls_shutouts_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/shutouts.csv')
mls_teams_2011 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2011/Teams/*.csv')

# 2012
mls_assist_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/assists.csv')
mls_fouls_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/fouls.csv')
mls_goal_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/goalkeeping.csv')
mls_saves_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/saves.csv')
mls_shots_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/shots.csv')
mls_shutouts_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/shutouts.csv')
mls_teams_2012 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2012/Teams/*.csv')

# 2013
mls_assist_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/assists.csv')
mls_fouls_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/fouls.csv')
mls_goal_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/goalkeeping.csv')
mls_saves_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/saves.csv')
mls_shots_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/shots.csv')
mls_shutouts_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/shutouts.csv')
mls_teams_2013 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2013/Teams/*.csv')

# 2014
mls_assist_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/assists.csv')
mls_fouls_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/fouls.csv')
mls_goal_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/goalkeeping.csv')
mls_saves_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/saves.csv')
mls_shots_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/shots.csv')
mls_shutouts_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/shutouts.csv')
mls_teams_2014 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2014/Teams/*.csv')

# 2015

mls_assist_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/assists.csv')
mls_fouls_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/fouls.csv')
mls_goal_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/goalkeeping.csv')
mls_saves_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/saves.csv')
mls_shots_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/shots.csv')
mls_shutouts_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/shutouts.csv')
mls_teams_2015 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2015/Teams/*.csv')

# 2016
mls_assist_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/assists.csv')
mls_fouls_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/fouls.csv')
mls_goal_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/goalkeeping.csv')
mls_saves_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/saves.csv')
mls_shots_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/shots.csv')
mls_shutouts_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/shutouts.csv')
mls_teams_2016 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2016/Teams/*.csv')

# 2017 
mls_assist_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/assists.csv')
mls_fouls_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/fouls.csv')
mls_goal_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/goalkeeping.csv')
mls_saves_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/saves.csv')
mls_shots_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/shots.csv')
mls_shutouts_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/shutouts.csv')
mls_teams_2017 = read_files('s3://sportsdatawarehouse/men_soccer/MLS/2017/Teams/*.csv')