--
-- PostgreSQL database dump
--

-- Dumped from database version 11.6
-- Dumped by pg_dump version 12.2

-- Started on 2020-06-24 11:53:15 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


SET default_tablespace = '';



CREATE TABLE afc_records (
    "Wins" bigint,
    "Losses" bigint,
    "Ties" bigint,
    "Year" bigint,
    "Team" text
);


ALTER TABLE afc_records

--
-- TOC entry 274 (class 1259 OID 17973)

--

CREATE TABLE afl_records (
    "Wins" bigint,
    "Losses" bigint,
    "Ties" bigint,
    "Year" bigint,
    "Team" text
);




--
-- TOC entry 275 (class 1259 OID 17979)
-- Name: defense_gamestatistics; Type: TABLE; Schema:
--

CREATE TABLE defense_gamestatistics (
    "Defense_game_stats_Rk" bigint,
    "Defense_game_stats_Team" text,
    "Defense_game_stats_G" bigint,
    "Defense_game_stats_Pts/G" double precision,
    "Defense_game_stats_TotPts" bigint,
    "Defense_game_stats_Scrm Plys" text,
    "Defense_game_stats_Yds/G" double precision,
    "Defense_game_stats_Yds/P" double precision,
    "Defense_game_stats_1st/G" double precision,
    "Defense_game_stats_3rd Md" text,
    "Defense_game_stats_3rd Att" text,
    "Defense_game_stats_3rd Pct" bigint,
    "Defense_game_stats_4th Md" text,
    "Defense_game_stats_4th Att" text,
    "Defense_game_stats_4th Pct" bigint,
    "Defense_game_stats_Pen" bigint,
    "Defense_game_stats_Pen Yds" text,
    "Defense_game_stats_ToP/G" text,
    "Defense_game_stats_FUM" text,
    "Defense_game_stats_Lost" text,
    "Defense_game_stats_Year" bigint
);


ALTER TABLE defense_gamestatistics

--
-- TOC entry 276 (class 1259 OID 17985)
-- Name: defense_interception; Type: TABLE; Schema:
--

CREATE TABLE defense_interception (
    "Defense_interceptions_Rk" bigint,
    "Defense_interceptions_Team" text,
    "Defense_interceptions_PDef" bigint,
    "Defense_interceptions_Int" bigint,
    "Defense_interceptions_TDs" bigint,
    "Defense_interceptions_Yds" bigint,
    "Defense_interceptions_Lng" text,
    "Defense_interceptions_Year" bigint
);


ALTER TABLE defense_interception

--
-- TOC entry 277 (class 1259 OID 17991)
-- Name: defense_pass; Type: TABLE; Schema:
--

CREATE TABLE defense_pass (
    "Defense_passing_Rk" bigint,
    "Defense_passing_Team" text,
    "Defense_passing_Comp" bigint,
    "Defense_passing_Att" bigint,
    "Defense_passing_Pct" double precision,
    "Defense_passing_Att/G" double precision,
    "Defense_passing_Yds" text,
    "Defense_passing_Avg" double precision,
    "Defense_passing_Yds/G" double precision,
    "Defense_passing_Int" bigint,
    "Defense_passing_1st" bigint,
    "Defense_passing_1stpct" double precision,
    "Defense_passing_Lng" text,
    "Defense_passing_20+" bigint,
    "Defense_passing_40+" bigint,
    "Defense_passing_Sck" bigint,
    "Defense_passing_Rate" double precision,
    "Defense_passing_Year" bigint
);


ALTER TABLE defense_pass

--
-- TOC entry 278 (class 1259 OID 17997)
-- Name: defense_receive; Type: TABLE; Schema:
--

CREATE TABLE defense_receive (
    "Defense_receiving_Rk" bigint,
    "Defense_receiving_Team" text,
    "Defense_receiving_Yds" text,
    "Defense_receiving_FUM" text,
    "Defense_receiving_Year" bigint
);


ALTER TABLE defense_receive

--
-- TOC entry 279 (class 1259 OID 18003)
-- Name: defense_rush; Type: TABLE; Schema:
--

CREATE TABLE defense_rush (
    "Defense_rushing_Rk" bigint,
    "Defense_rushing_Team" text,
    "Defense_rushing_Att" bigint,
    "Defense_rushing_Att/G" double precision,
    "Defense_rushing_Yds" text,
    "Defense_rushing_Avg" double precision,
    "Defense_rushing_Yds/G" double precision,
    "Defense_rushing_Lng" text,
    "Defense_rushing_1st" text,
    "Defense_rushing_1stpct" text,
    "Defense_rushing_20+" text,
    "Defense_rushing_40+" text,
    "Defense_rushing_FUM" text,
    "Defense_rushing_Year" bigint
);


ALTER TABLE defense_rush

--
-- TOC entry 280 (class 1259 OID 18009)
-- Name: defense_score; Type: TABLE; Schema:
--

CREATE TABLE defense_score (
    "Defense_scoring_Rk" bigint,
    "Defense_scoring_Team" text,
    "Defense_scoring_PRet" bigint,
    "Defense_scoring_KRet" bigint,
    "Defense_scoring_INT" bigint,
    "Defense_scoring_FUM" bigint,
    "Defense_scoring_Blk FG" bigint,
    "Defense_scoring_Blk Pnt" bigint,
    "Defense_scoring_XPM" bigint,
    "Defense_scoring_FGM" bigint,
    "Defense_scoring_SFTY" bigint,
    "Defense_scoring_2-PT" text,
    "Defense_scoring_Year" bigint
);


ALTER TABLE defense_score

--
-- TOC entry 281 (class 1259 OID 18015)
-- Name: defense_tackle; Type: TABLE; Schema:
--

CREATE TABLE defense_tackle (
    "Defense_tackles_Rk" bigint,
    "Defense_tackles_Team" text,
    "Defense_tackles_Comb" text,
    "Defense_tackles_Total" bigint,
    "Defense_tackles_Ast" bigint,
    "Defense_tackles_Sck" bigint,
    "Defense_tackles_FF" bigint,
    "Defense_tackles_Rec" text,
    "Defense_tackles_TD" text,
    "Defense_tackles_Year" bigint
);


ALTER TABLE defense_tackle;



CREATE TABLE men_internationalsoccer (
    home text,
    away text,
    date text,
    gh bigint,
    ga bigint,
    full_time text,
    competition text,
    home_ident text,
    away_ident text,
    home_country text,
    away_country text,
    home_code text,
    away_code text,
    home_continent text,
    away_continent text,
    continent text,
    level text,
    league text,
    sport text,
    gender text
);


ALTER TABLE men_internationalsoccer

--
-- TOC entry 242 (class 1259 OID 17611)
-- Name: men_tennis; Type: TABLE; Schema:

CREATE TABLE men_tennis (
    "ATP;Location;Tournament;Date;Series;Court;Surface;Round;Best of" text,
    league text,
    sport text,
    gender text
);


ALTER TABLE men_tennis

--
-- TOC entry 204 (class 1259 OID 16975)
-- Name: mlb_allstar_games; Type: TABLE; Schema:
--

CREATE TABLE mlb_allstar_games (
    "playerID" PRIMARY KEY ,
    "yearID" double precision,
    "gameNum" double precision,
    "gameID" text,
    "teamID" text,
    "lgID" text,
    "GP" bigint,
    "startingPos" double precision
);


ALTER TABLE mlb_allstar_games

--
-- TOC entry 205 (class 1259 OID 16981)
-- Name: mlb_appearances; Type: TABLE; Schema:
--

CREATE TABLE mlb_appearances (
    "yearID" bigint,
    "teamID" text,
    "lgID" text,
    "playerID" text,
    "G_all" bigint,
    "GS" double precision,
    "G_batting" bigint,
    "G_defense" double precision,
    "G_p" bigint,
    "G_c" bigint,
    "G_1b" bigint,
    "G_2b" bigint,
    "G_3b" bigint,
    "G_ss" bigint,
    "G_lf" bigint,
    "G_cf" bigint,
    "G_rf" bigint,
    "G_of" bigint,
    "G_dh" double precision,
    "G_ph" double precision,
    "G_pr" double precision
);


ALTER TABLE mlb_appearances

--
-- TOC entry 206 (class 1259 OID 16988)
-- Name: mlb_award_managers; Type: TABLE; Schema:
--

CREATE TABLE mlb_award_managers (
    "playerID" text,
    "awardID" text,
    "yearID" bigint,
    "lgID" text,
    tie text,
    notes text
);


ALTER TABLE mlb_award_managers

--
-- TOC entry 207 (class 1259 OID 16994)
-- Name: mlb_award_players; Type: TABLE; Schema:
--

CREATE TABLE mlb_award_players (
    "awardID" text,
    "yearID" bigint,
    "lgID" text,
    "playerID" text,
    "pointsWon" bigint,
    "pointsMax" double precision,
    "votesFirst" bigint
);


ALTER TABLE mlb_award_players

--
-- TOC entry 208 (class 1259 OID 17000)
-- Name: mlb_awardshared_players; Type: TABLE; Schema:
--

CREATE TABLE mlb_awardshared_players (
    "awardID" text,
    "yearID" bigint,
    "lgID" text,
    "playerID" text,
    "pointsWon" double precision,
    "pointsMax" bigint,
    "votesFirst" double precision
);


ALTER TABLE mlb_awardshared_players

--
-- TOC entry 209 (class 1259 OID 17006)
-- Name: mlb_batting; Type: TABLE; Schema:
--

CREATE TABLE mlb_batting (
    "playerID" text,
    "yearID" bigint,
    stint bigint,
    "teamID" text,
    "lgID" text,
    "G" bigint,
    "AB" bigint,
    "R" bigint,
    "H" bigint,
    "2B" bigint,
    "3B" bigint,
    "HR" bigint,
    "RBI" double precision,
    "SB" double precision,
    "CS" double precision,
    "BB" bigint,
    "SO" double precision,
    "IBB" double precision,
    "HBP" double precision,
    "SH" double precision,
    "SF" double precision,
    "GIDP" double precision
);


ALTER TABLE mlb_batting

--
-- TOC entry 211 (class 1259 OID 17018)
-- Name: mlb_fielding; Type: TABLE; Schema:
--

CREATE TABLE mlb_fielding (
    "playerID" text,
    "yearID" bigint,
    stint bigint,
    "teamID" text,
    "lgID" text,
    "POS" text,
    "G" bigint,
    "GS" double precision,
    "InnOuts" double precision,
    "PO" bigint,
    "A" bigint,
    "E" double precision,
    "DP" bigint,
    "PB" double precision,
    "WP" double precision,
    "SB" double precision,
    "CS" double precision,
    "ZR" double precision
);


ALTER TABLE mlb_fielding

--
-- TOC entry 212 (class 1259 OID 17025)
-- Name: mlb_fieldingof; Type: TABLE; Schema:
--

CREATE TABLE mlb_fieldingof (
    "playerID" text,
    "yearID" bigint,
    stint bigint,
    "Glf" double precision,
    "Gcf" double precision,
    "Grf" double precision
);


ALTER TABLE mlb_fieldingof

--
-- TOC entry 213 (class 1259 OID 17031)
-- Name: mlb_fieldingpost; Type: TABLE; Schema:
--

CREATE TABLE mlb_fieldingpost (
    "playerID" text,
    "yearID" bigint,
    "teamID" text,
    "lgID" text,
    round text,
    "POS" text,
    "G" bigint,
    "GS" bigint,
    "InnOuts" bigint,
    "PO" bigint,
    "A" bigint,
    "E" bigint,
    "DP" bigint,
    "TP" bigint,
    "PB" double precision,
    "SB" double precision,
    "CS" double precision
);


ALTER TABLE mlb_fieldingpost

--
-- TOC entry 214 (class 1259 OID 17037)
-- Name: mlb_halloffame; Type: TABLE; Schema:
--

CREATE TABLE mlb_halloffame (
    "playerID" text,
    "yearID" bigint,
    "votedBy" text,
    ballots double precision,
    needed double precision,
    votes double precision,
    inducted text,
    category text,
    needed_note text
);


ALTER TABLE mlb_halloffame

--
-- TOC entry 215 (class 1259 OID 17043)
-- Name: mlb_homegames; Type: TABLE; Schema:
--

CREATE TABLE mlb_homegames (
    "year.key" bigint,
    "league.key" text,
    "team.key" text,
    "park.key" text,
    "span.first" text,
    "span.last" text,
    games bigint,
    openings bigint,
    attendance bigint
);


ALTER TABLE mlb_homegames

--
-- TOC entry 216 (class 1259 OID 17049)
-- Name: mlb_managers; Type: TABLE; Schema:
--

CREATE TABLE mlb_managers (
    "playerID" text,
    "yearID" bigint,
    "teamID" text,
    "lgID" text,
    inseason bigint,
    "G" bigint,
    "W" bigint,
    "L" bigint,
    rank double precision,
    "plyrMgr" text
);


ALTER TABLE mlb_managers

--
-- TOC entry 217 (class 1259 OID 17055)
-- Name: mlb_parks; Type: TABLE; Schema:
--

CREATE TABLE mlb_parks (
    "park.key" text,
    "park.name" text,
    "park.alias" text,
    city text,
    state text,
    country text
);


ALTER TABLE mlb_parks

--
-- TOC entry 218 (class 1259 OID 17061)
-- Name: mlb_players; Type: TABLE; Schema:
--

CREATE TABLE mlb_players (
    "playerID" text,
    "birthYear" bigint,
    "birthMonth" bigint,
    "birthDay" bigint,
    "birthCountry" text,
    "birthState" text,
    "birthCity" text,
    "deathYear" bigint,
    "deathMonth" bigint,
    "deathDay" bigint,
    "deathCountry" text,
    "deathState" text,
    "deathCity" text,
    "nameFirst" text,
    "nameLast" text,
    "nameGiven" text,
    weight bigint,
    height bigint,
    bats text,
    throws text,
    debut text,
    "finalGame" text,
    "retroID" text,
    "bbrefID" text
);


ALTER TABLE mlb_players

--
-- TOC entry 210 (class 1259 OID 17012)
-- Name: mlb_postbatting; Type: TABLE; Schema:
--

CREATE TABLE mlb_postbatting (
    "yearID" bigint,
    round text,
    "playerID" text,
    "teamID" text,
    "lgID" text,
    "G" bigint,
    "AB" bigint,
    "R" bigint,
    "H" bigint,
    "2B" bigint,
    "3B" bigint,
    "HR" bigint,
    "RBI" bigint,
    "SB" bigint,
    "CS" double precision,
    "BB" bigint,
    "SO" bigint,
    "IBB" bigint,
    "HBP" double precision,
    "SH" double precision,
    "SF" double precision,
    "GIDP" double precision
);


ALTER TABLE mlb_postbatting

--
-- TOC entry 219 (class 1259 OID 17068)
-- Name: mlb_teams; Type: TABLE; Schema:
--

CREATE TABLE mlb_teams (
    "yearID" bigint,
    "teamID" text,
    "franchID" text,
    "Rank" bigint,
    "G" bigint,
    "Ghome" double precision,
    "W" bigint,
    "L" bigint,
    "DivWin" text,
    "WCWin" text,
    "LgWin" text,
    "WSWin" text,
    "R" bigint,
    "AB" bigint,
    "H" bigint,
    "2B" bigint,
    "3B" bigint,
    "HR" bigint,
    "BB" double precision,
    "SO" double precision,
    "SB" double precision,
    "CS" double precision,
    "HBP" double precision,
    "SF" double precision,
    "RA" bigint,
    "ER" bigint,
    "ERA" double precision,
    "CG" bigint,
    "SHO" bigint,
    "SV" bigint,
    "IPouts" bigint,
    "HA" bigint,
    "HRA" bigint,
    "BBA" bigint,
    "SOA" bigint,
    "E" bigint,
    "DP" bigint,
    "FP" double precision,
    name text,
    park text,
    attendance double precision,
    "BPF" bigint,
    "PPF" bigint,
    "teamIDBR" text,
    "teamIDlahman45" text,
    "teamIDretro" text,
    league text,
    sport text,
    gender text
);


ALTER TABLE mlb_teams

--
-- TOC entry 220 (class 1259 OID 17074)
-- Name: mlb_teams_franchise; Type: TABLE; Schema:
--

CREATE TABLE mlb_teams_franchise (
    "franchID" text,
    "franchName" text,
    active text,
    "NAassoc" text
);


ALTER TABLE mlb_teams_franchise

--
-- TOC entry 245 (class 1259 OID 17661)
-- Name: mncaa_cities; Type: TABLE; Schema:
--

CREATE TABLE mncaa_cities (
    city_id bigint,
    city text,
    state text
);


ALTER TABLE mncaa_cities

--
-- TOC entry 246 (class 1259 OID 17667)
-- Name: mncaa_coaches; Type: TABLE; Schema:
--

CREATE TABLE mncaa_coaches (
    season bigint,
    team_id bigint,
    first_day bigint,
    last_day bigint,
    coach_name text
);


ALTER TABLE mncaa_coaches

--
-- TOC entry 247 (class 1259 OID 17674)
-- Name: mncaa_conference; Type: TABLE; Schema:
--

CREATE TABLE mncaa_conference (
    conf_abbrev text,
    description text
);


ALTER TABLE mncaa_conference

--
-- TOC entry 248 (class 1259 OID 17681)
-- Name: mncaa_conference_games; Type: TABLE; Schema:
--

CREATE TABLE mncaa_conference_games (
    season bigint,
    conf_abbrev text,
    day bigint,
    win_teamid bigint,
    l_teamid bigint
);


ALTER TABLE mncaa_conference_games

--
-- TOC entry 264 (class 1259 OID 17779)
-- Name: mncaa_events; Type: TABLE; Schema:
--

CREATE TABLE mncaa_events (
    event_id bigint,
    season bigint,
    day bigint,
    winning_teamid bigint,
    losing_teamid bigint,
    winning_points bigint,
    losing_points bigint,
    elapsed_seconds bigint,
    event_teamid bigint,
    event_playerid bigint,
    event_type text,
    league text,
    gender text,
    sport text
);


ALTER TABLE mncaa_events

--
-- TOC entry 249 (class 1259 OID 17687)
-- Name: mncaa_gamecities; Type: TABLE; Schema:
--

CREATE TABLE mncaa_gamecities (
    season bigint,
    day bigint,
    win_teamid bigint,
    l_team_id bigint,
    event_type text,
    city_id bigint
);


ALTER TABLE mncaa_gamecities

--
-- TOC entry 244 (class 1259 OID 17655)
-- Name: mncaa_players; Type: TABLE; Schema:
--

CREATE TABLE mncaa_players (
    player_id bigint,
    season bigint,
    team_id bigint,
    player_name text
);


ALTER TABLE mncaa_players

--
-- TOC entry 250 (class 1259 OID 17693)
-- Name: mncaa_seasongames; Type: TABLE; Schema:
--

CREATE TABLE mncaa_seasongames (
    season bigint,
    day bigint,
    winning_teamid bigint,
    winning_score bigint,
    losing_teamid bigint,
    losing_score bigint,
    winning_teamlocation text,
    total_overtime_pd bigint,
    winning_fieldgoals bigint,
    win_fieldgoal_attmpt bigint,
    win_3fieldgoals bigint,
    "win_fieldgoal_attmpt.1" bigint,
    win_freethrows bigint,
    win_freethrows_attmpt bigint,
    win_offensiverebounds bigint,
    win_defensiverebounds bigint,
    win_assists bigint,
    win_turnovers bigint,
    win_steals bigint,
    win_blocks bigint,
    win_personalfouls bigint,
    "winning_fieldgoals.1" bigint,
    l_fieldgoal_attmpt bigint,
    l_3fieldgoals bigint,
    "l_fieldgoal_attmpt.1" bigint,
    l_freethrows bigint,
    l_freethrows_attmpt bigint,
    l_offensiverebounds bigint,
    l_defensiverebounds bigint,
    l_assists bigint,
    l_turnovers bigint,
    l_steals bigint,
    l_blocks bigint,
    l_personalfouls bigint
);


ALTER TABLE mncaa_seasongames

--
-- TOC entry 252 (class 1259 OID 17705)
-- Name: mncaa_team; Type: TABLE; Schema:
--

CREATE TABLE mncaa_team (
    team_id bigint,
    team_name text,
    firstd1_season bigint,
    " lastd1_season" bigint
);


ALTER TABLE mncaa_team

--
-- TOC entry 251 (class 1259 OID 17699)
-- Name: mncaa_teamconference; Type: TABLE; Schema:
--

CREATE TABLE mncaa_teamconference (
    season bigint,
    team_id bigint,
    conf_abbrev text
);


ALTER TABLE mncaa_teamconference

--
-- TOC entry 253 (class 1259 OID 17711)
-- Name: mncaa_tournament; Type: TABLE; Schema:
--

CREATE TABLE mncaa_tournament (
    season bigint,
    day bigint,
    winning_teamid bigint,
    winning_score bigint,
    losing_teamid bigint,
    losing_score bigint,
    winning_teamlocation text,
    total_overtime_pd bigint,
    winning_fieldgoals bigint,
    win_fieldgoal_attmpt bigint,
    win_3fieldgoals bigint,
    "win_fieldgoal_attmpt.1" bigint,
    win_freethrows bigint,
    win_freethrows_attmpt bigint,
    win_offensiverebounds bigint,
    win_defensiverebounds bigint,
    win_assists bigint,
    win_turnovers bigint,
    win_steals bigint,
    win_blocks bigint,
    win_personalfouls bigint,
    "winning_fieldgoals.1" bigint,
    l_fieldgoal_attmpt bigint,
    l_3fieldgoals bigint,
    "l_fieldgoal_attmpt.1" bigint,
    l_freethrows bigint,
    l_freethrows_attmpt bigint,
    l_offensiverebounds bigint,
    l_defensiverebounds bigint,
    l_assists bigint,
    l_turnovers bigint,
    l_steals bigint,
    l_blocks bigint,
    l_personalfouls bigint
);


ALTER TABLE mncaa_tournament

--
-- TOC entry 297 (class 1259 OID 18111)
-- Name: nba_game_details; Type: TABLE; Schema:
--

CREATE TABLE nba_game_details (
    "GAME_ID" bigint,
    "TEAM_ID" bigint,
    "TEAM_ABBREVIATION" text,
    "TEAM_CITY" text,
    "PLAYER_ID" bigint,
    "PLAYER_NAME" text,
    "START_POSITION" text,
    "COMMENT" text,
    "MIN" text,
    "FGM" double precision,
    "FGA" double precision,
    "FG_PCT" double precision,
    "FG3M" double precision,
    "FG3A" double precision,
    "FG3_PCT" double precision,
    "FTM" double precision,
    "FTA" double precision,
    "FT_PCT" double precision,
    "OREB" double precision,
    "DREB" double precision,
    "REB" double precision,
    "AST" double precision,
    "STL" double precision,
    "BLK" double precision,
    "TO" double precision,
    "PF" double precision,
    "PTS" double precision,
    "PLUS_MINUS" double precision
);


ALTER TABLE nba_game_details

--
-- TOC entry 229 (class 1259 OID 17399)
-- Name: nba_player_list; Type: TABLE; Schema:
--

CREATE TABLE nba_player_list (
    "Player" text,
    player_id bigint
);


ALTER TABLE nba_player_list

--
-- TOC entry 231 (class 1259 OID 17411)
-- Name: nba_players; Type: TABLE; Schema:
--

CREATE TABLE nba_players (
    "Player" text,
    "Pos" text,
    "Age" double precision,
    "Tm" text,
    season bigint,
    statistic_name text,
    statistic double precision
);


ALTER TABLE nba_players

--
-- TOC entry 230 (class 1259 OID 17405)
-- Name: nba_players_norm; Type: TABLE; Schema:
--

CREATE TABLE nba_players_norm (
    "Player" text,
    "Pos" text,
    "Age" double precision,
    "Tm" text,
    "G" double precision,
    "GS" double precision,
    "MP" double precision,
    "FG" double precision,
    "FGA" double precision,
    "FG_pct" double precision,
    "3P" double precision,
    "3PA" double precision,
    "3P_pct" double precision,
    "2P" double precision,
    "2PA" double precision,
    "2P_pct" double precision,
    "eFG_pct" double precision,
    "FT" double precision,
    "FTA" double precision,
    "FT_pct" double precision,
    "ORB" double precision,
    "DRB" double precision,
    "TRB" double precision,
    "AST" double precision,
    "STL" double precision,
    "BLK" double precision,
    "TOV" double precision,
    "PF" double precision,
    "PTS" double precision,
    season bigint
);


ALTER TABLE nba_players_norm

--
-- TOC entry 232 (class 1259 OID 17425)
-- Name: nba_salary; Type: TABLE; Schema:
--

CREATE TABLE nba_salary (
    "Name" text,
    "Team" text,
    "Salary" bigint
);


ALTER TABLE nba_salary

--
-- TOC entry 228 (class 1259 OID 17393)
-- Name: nba_team_list; Type: TABLE; Schema:
--

CREATE TABLE nba_team_list (
    "Team" text,
    team_id bigint
);


ALTER TABLE nba_team_list

--
-- TOC entry 227 (class 1259 OID 17387)
-- Name: nba_teams; Type: TABLE; Schema:
--

CREATE TABLE nba_teams (
    "Team" text,
    season bigint,
    league text,
    sport text,
    gender text,
    statistic_name text,
    statistic double precision
);


ALTER TABLE nba_teams

--
-- TOC entry 238 (class 1259 OID 17482)
-- Name: nba_teamsids; Type: TABLE; Schema:
--

CREATE TABLE nba_teamsids (
    "Tm" text,
    "Team" text,
    team_id bigint
);


ALTER TABLE nba_teamsids

--
-- TOC entry 282 (class 1259 OID 18021)
-- Name: nfc_records; Type: TABLE; Schema:
--

CREATE TABLE nfc_records (
    "Wins" bigint,
    "Losses" bigint,
    "Ties" bigint,
    "Year" bigint,
    "Team" text
);


ALTER TABLE nfc_records

--
-- TOC entry 265 (class 1259 OID 17842)
-- Name: nfl_game; Type: TABLE; Schema:
--

CREATE TABLE nfl_game (
    away_score double precision,
    away_team text,
    game_id bigint,
    game_url text,
    gender text,
    home_score double precision,
    home_team text,
    season bigint,
    sport text,
    sport_league text,
    state_of_game text,
    type text,
    week bigint
);


ALTER TABLE nfl_game

--
-- TOC entry 270 (class 1259 OID 17877)
-- Name: nfl_passing_game; Type: TABLE; Schema:
--

CREATE TABLE nfl_passing_game (
    "GameID" bigint,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Attempts" bigint,
    "Completions" bigint,
    "Drives" bigint,
    "Comp_Perc" double precision,
    "Total_Yards" bigint,
    "Total_Raw_AirYards" bigint,
    "Total_Comp_AirYards" bigint,
    "Yards_per_Att" double precision,
    "Yards_per_Comp" double precision,
    "Yards_per_Drive" double precision,
    "Raw_AirYards_per_Att" double precision,
    "Comp_AirYards_per_Att" double precision,
    "Raw_AirYards_per_Comp" double precision,
    "Comp_AirYards_per_Comp" double precision,
    "Raw_AirYards_per_Drive" double precision,
    "Comp_AirYards_per_Drive" double precision,
    "PACR" double precision,
    "TimesHit" bigint,
    "TimesHit_per_Drive" double precision,
    "Interceptions" bigint,
    "TDs" bigint,
    "Air_TDs" bigint,
    "aPACR" double precision,
    "Air_TD_Rate" double precision,
    "TD_to_Int" double precision,
    "Total_EPA" double precision,
    "Success_Rate" double precision,
    "EPA_per_Att" double precision,
    "EPA_per_Comp" double precision,
    "EPA_Comp_Perc" double precision,
    "TD_per_Att" double precision,
    "Air_TD_per_Att" double precision,
    "Int_per_Att" double precision,
    "TD_per_Comp" double precision,
    "Air_TD_per_Comp" double precision,
    "TD_per_Drive" double precision,
    "Air_TD_per_Drive" double precision,
    "Int_per_Drive" double precision,
    "EPA_per_Drive" double precision,
    "Total_WPA" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Att" double precision,
    "WPA_per_Comp" double precision,
    "WPA_Comp_Perc" double precision,
    "WPA_per_Drive" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Att" double precision,
    "Clutch_EPA_per_Drive" double precision,
    "airEPA_Comp" double precision,
    "airEPA_Incomp" double precision,
    "Total_Raw_airEPA" double precision,
    "Raw_airEPA_per_Att" double precision,
    "Raw_airEPA_per_Drive" double precision,
    "epa_PACR" double precision,
    "airEPA_per_Att" double precision,
    "airEPA_per_Comp" double precision,
    "airEPA_per_Drive" double precision,
    "air_Success_Rate" double precision,
    "air_Comp_Success_Rate" double precision,
    "airWPA_Comp" double precision,
    "airWPA_Incomp" double precision,
    "Total_Raw_airWPA" double precision,
    "wpa_PACR" double precision,
    "Raw_airWPA_per_Att" double precision,
    "Raw_airWPA_per_Drive" double precision,
    "airWPA_per_Att" double precision,
    "airWPA_per_Comp" double precision,
    "airWPA_per_Drive" double precision,
    "air_Win_Success_Rate" double precision,
    "air_Comp_Win_Success_Rate" double precision,
    "yacEPA_Comp" double precision,
    "yacEPA_Drop" double precision,
    "Total_yacEPA" double precision,
    "yacEPA_per_Att" double precision,
    "yacEPA_per_Comp" double precision,
    "yacEPA_Rec_per_Drive" double precision,
    "yacEPA_Drop_per_Drive" double precision,
    "yacWPA_Comp" double precision,
    "yacWPA_Drop" double precision,
    "Total_yacWPA" double precision,
    "yacWPA_per_Att" double precision,
    "yacWPA_per_Comp" double precision,
    "yacWPA_Comp_per_Drive" double precision,
    "yacWPA_Drop_per_Drive" double precision,
    "yac_Success_Rate" double precision,
    "yac_Rec_Success_Rate" double precision,
    "yac_Win_Success_Rate" double precision,
    "yac_Comp_Win_Success_Rate" double precision
);


ALTER TABLE nfl_passing_game

--
-- TOC entry 267 (class 1259 OID 17854)
-- Name: nfl_passing_player; Type: TABLE; Schema:
--

CREATE TABLE nfl_passing_player (
    "GameID" bigint,
    "Passer_ID" text,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Attempts" bigint,
    "Completions" bigint,
    "Drives" bigint,
    "Comp_Perc" double precision,
    "Total_Yards" bigint,
    "Total_Raw_AirYards" bigint,
    "Total_Comp_AirYards" bigint,
    "Yards_per_Att" double precision,
    "Yards_per_Comp" double precision,
    "Yards_per_Drive" double precision,
    "Raw_AirYards_per_Att" double precision,
    "Comp_AirYards_per_Att" double precision,
    "Raw_AirYards_per_Comp" double precision,
    "Comp_AirYards_per_Comp" double precision,
    "Raw_AirYards_per_Drive" double precision,
    "Comp_AirYards_per_Drive" double precision,
    "PACR" double precision,
    "TimesHit" bigint,
    "TimesHit_per_Drive" double precision,
    "Interceptions" bigint,
    "TDs" bigint,
    "Air_TDs" bigint,
    "aPACR" double precision,
    "Air_TD_Rate" double precision,
    "TD_to_Int" double precision,
    "Total_EPA" double precision,
    "Success_Rate" double precision,
    "EPA_per_Att" double precision,
    "EPA_per_Comp" double precision,
    "EPA_Comp_Perc" double precision,
    "TD_per_Att" double precision,
    "Air_TD_per_Att" double precision,
    "Int_per_Att" double precision,
    "TD_per_Comp" double precision,
    "Air_TD_per_Comp" double precision,
    "TD_per_Drive" double precision,
    "Air_TD_per_Drive" double precision,
    "Int_per_Drive" double precision,
    "EPA_per_Drive" double precision,
    "Total_WPA" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Att" double precision,
    "WPA_per_Comp" double precision,
    "WPA_Comp_Perc" double precision,
    "WPA_per_Drive" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Att" double precision,
    "Clutch_EPA_per_Drive" double precision,
    "airEPA_Comp" double precision,
    "airEPA_Incomp" double precision,
    "Total_Raw_airEPA" double precision,
    "Raw_airEPA_per_Att" double precision,
    "Raw_airEPA_per_Drive" double precision,
    "epa_PACR" double precision,
    "airEPA_per_Att" double precision,
    "airEPA_per_Comp" double precision,
    "airEPA_per_Drive" double precision,
    "air_Success_Rate" double precision,
    "air_Comp_Success_Rate" double precision,
    "airWPA_Comp" double precision,
    "airWPA_Incomp" double precision,
    "Total_Raw_airWPA" double precision,
    "wpa_PACR" double precision,
    "Raw_airWPA_per_Att" double precision,
    "Raw_airWPA_per_Drive" double precision,
    "airWPA_per_Att" double precision,
    "airWPA_per_Comp" double precision,
    "airWPA_per_Drive" double precision,
    "air_Win_Success_Rate" double precision,
    "air_Comp_Win_Success_Rate" double precision,
    "yacEPA_Comp" double precision,
    "yacEPA_Drop" double precision,
    "Total_yacEPA" double precision,
    "yacEPA_per_Att" double precision,
    "yacEPA_per_Comp" double precision,
    "yacEPA_Rec_per_Drive" double precision,
    "yacEPA_Drop_per_Drive" double precision,
    "yacWPA_Comp" double precision,
    "yacWPA_Drop" double precision,
    "Total_yacWPA" double precision,
    "yacWPA_per_Att" double precision,
    "yacWPA_per_Comp" double precision,
    "yacWPA_Comp_per_Drive" double precision,
    "yacWPA_Drop_per_Drive" double precision,
    "yac_Success_Rate" double precision,
    "yac_Rec_Success_Rate" double precision,
    "yac_Win_Success_Rate" double precision,
    "yac_Comp_Win_Success_Rate" double precision
);


ALTER TABLE nfl_passing_player

--
-- TOC entry 271 (class 1259 OID 17883)
-- Name: nfl_receiving_game; Type: TABLE; Schema:
--

CREATE TABLE nfl_receiving_game (
    "GameID" bigint,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Targets" bigint,
    "Receptions" bigint,
    "Drives" bigint,
    "Targets_per_Drive" double precision,
    "Rec_per_Drive" double precision,
    "Total_Yards" bigint,
    "Yards_per_Drive" double precision,
    "Total_Raw_YAC" bigint,
    "Yards_per_Rec" double precision,
    "Yards_per_Target" double precision,
    "YAC_per_Target" double precision,
    "Total_Caught_YAC" bigint,
    "Total_Dropped_YAC" bigint,
    "Caught_YAC_per_Target" double precision,
    "Dropped_YAC_per_Target" double precision,
    "YAC_per_Rec" double precision,
    "Caught_YAC_per_Rec" double precision,
    "Dropped_YAC_per_Rec" double precision,
    "YAC_per_Drive" double precision,
    "Caught_YAC_per_Drive" double precision,
    "Dropped_YAC_per_Drive" double precision,
    "Rec_Percentage" double precision,
    "Fumbles" bigint,
    "TDs" bigint,
    "TDs_per_Drive" double precision,
    "Fumbles_per_Drive" double precision,
    "AC_TDs" bigint,
    "AC_TDs_per_Drive" double precision,
    "AC_TD_Rate" double precision,
    "TD_to_Fumbles" double precision,
    "Total_EPA" double precision,
    "EPA_per_Drives" double precision,
    "Success_Rate" double precision,
    "EPA_per_Rec" double precision,
    "EPA_per_Target" double precision,
    "EPA_Rec_Perc" double precision,
    "TD_per_Targets" double precision,
    "Fumbles_per_Rec" double precision,
    "TD_per_Rec" double precision,
    "Total_WPA" double precision,
    "WPA_per_Drive" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Target" double precision,
    "WPA_per_Rec" double precision,
    "WPA_Rec_Perc" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Drive" double precision,
    "Total_Raw_AirYards" bigint,
    "PACR" double precision,
    "Total_Caught_AirYards" bigint,
    "Raw_AirYards_per_Target" double precision,
    "RACR" double precision,
    "Total_Raw_airEPA" double precision,
    "Total_Caught_airEPA" double precision,
    "Raw_airEPA_per_Drive" double precision,
    "Caught_airEPA_per_Drive" double precision,
    "airEPA_per_Target" double precision,
    "Caught_airEPA_per_Target" double precision,
    "epa_RACR" double precision,
    "Total_Raw_airWPA" double precision,
    "Total_Caught_airWPA" double precision,
    "Raw_airWPA_per_Drive" double precision,
    "Caught_airWPA_per_Drive" double precision,
    "airWPA_per_Target" double precision,
    "Caught_airWPA_per_Target" double precision,
    "yacEPA_Rec" double precision,
    "yacEPA_Drop" double precision,
    "Total_yacEPA" double precision,
    "yacEPA_per_Target" double precision,
    "yacEPA_per_Rec" double precision,
    "yacEPA_Rec_per_Drive" double precision,
    "yacEPA_Drop_per_Drive" double precision,
    "yacWPA_Rec" double precision,
    "yacWPA_Drop" double precision,
    "Total_yacWPA" double precision,
    "yacWPA_per_Target" double precision,
    "yacWPA_per_Rec" double precision,
    "yacWPA_Rec_per_Drive" double precision,
    "yacWPA_Drop_per_Drive" double precision,
    "wpa_RACR" double precision,
    "yac_Success_Rate" double precision,
    "yac_Rec_Success_Rate" double precision,
    "air_Success_Rate" double precision,
    "air_Rec_Success_Rate" double precision,
    "yac_Win_Success_Rate" double precision,
    "yac_Rec_Win_Success_Rate" double precision,
    "air_Win_Success_Rate" double precision,
    "air_Rec_Win_Success_Rate" double precision
);


ALTER TABLE nfl_receiving_game

--
-- TOC entry 268 (class 1259 OID 17860)
-- Name: nfl_receiving_player; Type: TABLE; Schema:
--

CREATE TABLE nfl_receiving_player (
    "GameID" bigint,
    "Receiver_ID" text,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Targets" bigint,
    "Receptions" bigint,
    "Drives" bigint,
    "Targets_per_Drive" double precision,
    "Rec_per_Drive" double precision,
    "Total_Yards" bigint,
    "Yards_per_Drive" double precision,
    "Total_Raw_YAC" bigint,
    "Yards_per_Rec" double precision,
    "Yards_per_Target" double precision,
    "YAC_per_Target" double precision,
    "Total_Caught_YAC" bigint,
    "Total_Dropped_YAC" bigint,
    "Caught_YAC_per_Target" double precision,
    "Dropped_YAC_per_Target" double precision,
    "YAC_per_Rec" double precision,
    "Caught_YAC_per_Rec" double precision,
    "Dropped_YAC_per_Rec" double precision,
    "YAC_per_Drive" double precision,
    "Caught_YAC_per_Drive" double precision,
    "Dropped_YAC_per_Drive" double precision,
    "Rec_Percentage" double precision,
    "Fumbles" bigint,
    "TDs" bigint,
    "TDs_per_Drive" double precision,
    "Fumbles_per_Drive" double precision,
    "AC_TDs" bigint,
    "AC_TDs_per_Drive" double precision,
    "AC_TD_Rate" double precision,
    "TD_to_Fumbles" double precision,
    "Total_EPA" double precision,
    "EPA_per_Drives" double precision,
    "Success_Rate" double precision,
    "EPA_per_Rec" double precision,
    "EPA_per_Target" double precision,
    "EPA_Rec_Perc" double precision,
    "TD_per_Targets" double precision,
    "Fumbles_per_Rec" double precision,
    "TD_per_Rec" double precision,
    "Total_WPA" double precision,
    "WPA_per_Drive" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Target" double precision,
    "WPA_per_Rec" double precision,
    "WPA_Rec_Perc" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Drive" double precision,
    "Total_Raw_AirYards" bigint,
    "PACR" double precision,
    "Total_Caught_AirYards" bigint,
    "Raw_AirYards_per_Target" double precision,
    "RACR" double precision,
    "Total_Raw_airEPA" double precision,
    "Total_Caught_airEPA" double precision,
    "Raw_airEPA_per_Drive" double precision,
    "Caught_airEPA_per_Drive" double precision,
    "airEPA_per_Target" double precision,
    "Caught_airEPA_per_Target" double precision,
    "epa_RACR" double precision,
    "Total_Raw_airWPA" double precision,
    "Total_Caught_airWPA" double precision,
    "Raw_airWPA_per_Drive" double precision,
    "Caught_airWPA_per_Drive" double precision,
    "airWPA_per_Target" double precision,
    "Caught_airWPA_per_Target" double precision,
    "yacEPA_Rec" double precision,
    "yacEPA_Drop" double precision,
    "Total_yacEPA" double precision,
    "yacEPA_per_Target" double precision,
    "yacEPA_per_Rec" double precision,
    "yacEPA_Rec_per_Drive" double precision,
    "yacEPA_Drop_per_Drive" double precision,
    "yacWPA_Rec" double precision,
    "yacWPA_Drop" double precision,
    "Total_yacWPA" double precision,
    "yacWPA_per_Target" double precision,
    "yacWPA_per_Rec" double precision,
    "yacWPA_Rec_per_Drive" double precision,
    "yacWPA_Drop_per_Drive" double precision,
    "wpa_RACR" double precision,
    "yac_Success_Rate" double precision,
    "yac_Rec_Success_Rate" double precision,
    "air_Success_Rate" double precision,
    "air_Rec_Success_Rate" double precision,
    "yac_Win_Success_Rate" double precision,
    "yac_Rec_Win_Success_Rate" double precision,
    "air_Win_Success_Rate" double precision,
    "air_Rec_Win_Success_Rate" double precision
);


ALTER TABLE nfl_receiving_player

--
-- TOC entry 283 (class 1259 OID 18027)
-- Name: nfl_records; Type: TABLE; Schema:
--

CREATE TABLE nfl_records (
    "Wins" bigint,
    "Losses" bigint,
    "Ties" bigint,
    "Year" bigint,
    "Team" text
);


ALTER TABLE nfl_records

--
-- TOC entry 266 (class 1259 OID 17848)
-- Name: nfl_roster; Type: TABLE; Schema:
--

CREATE TABLE nfl_roster (
    season_type text,
    full_player_name text,
    abbr_player_name text,
    team text,
    "position" text,
    gsis_id text
);


ALTER TABLE nfl_roster

--
-- TOC entry 272 (class 1259 OID 17889)
-- Name: nfl_rushing_game; Type: TABLE; Schema:
--

CREATE TABLE nfl_rushing_game (
    "GameID" bigint,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Carries" bigint,
    "Drives" bigint,
    "Car_per_Drive" double precision,
    "Total_Yards" bigint,
    "Yards_per_Car" double precision,
    "Yards_per_Drive" double precision,
    "Fumbles" bigint,
    "TDs" bigint,
    "TD_to_Fumbles" double precision,
    "Total_EPA" double precision,
    "Success_Rate" double precision,
    "EPA_per_Car" double precision,
    "EPA_Ratio" double precision,
    "TD_per_Car" double precision,
    "Fumbles_per_Car" double precision,
    "Fumbles_per_Drive" double precision,
    "TD_Drive" double precision,
    "EPA_per_Drive" double precision,
    "Total_WPA" double precision,
    "WPA_per_Drive" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Car" double precision,
    "WPA_Ratio" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Car" double precision,
    "Clutch_EPA_per_Drive" double precision
);


ALTER TABLE nfl_rushing_game

--
-- TOC entry 269 (class 1259 OID 17871)
-- Name: nfl_rushing_player; Type: TABLE; Schema:
--

CREATE TABLE nfl_rushing_player (
    "GameID" bigint,
    "Rusher_ID" text,
    "Team" text,
    "Opponent" text,
    "Player_Name" text,
    "Carries" bigint,
    "Drives" bigint,
    "Car_per_Drive" double precision,
    "Total_Yards" bigint,
    "Yards_per_Car" double precision,
    "Yards_per_Drive" double precision,
    "Fumbles" bigint,
    "TDs" bigint,
    "TD_to_Fumbles" double precision,
    "Total_EPA" double precision,
    "Success_Rate" double precision,
    "EPA_per_Car" double precision,
    "EPA_Ratio" double precision,
    "TD_per_Car" double precision,
    "Fumbles_per_Car" double precision,
    "Fumbles_per_Drive" double precision,
    "TD_Drive" double precision,
    "EPA_per_Drive" double precision,
    "Total_WPA" double precision,
    "WPA_per_Drive" double precision,
    "Win_Success_Rate" double precision,
    "WPA_per_Car" double precision,
    "WPA_Ratio" double precision,
    "Total_Clutch_EPA" double precision,
    "Clutch_EPA_per_Car" double precision,
    "Clutch_EPA_per_Drive" double precision
);


ALTER TABLE nfl_rushing_player

--
-- TOC entry 295 (class 1259 OID 18099)
-- Name: offense_defense; Type: TABLE; Schema:
--

CREATE TABLE offense_defense (
    "Team" text,
    "Year" bigint,
    "Superbowl_Winner" bigint,
    "Superbowl_Loser_Team" text,
    "Superbowl_Loser" bigint,
    "Wins" bigint,
    "Losses" bigint,
    "Ties" bigint,
    "Offense_touchdowns_Rk" bigint,
    "Offense_touchdowns_Total" bigint,
    "Offense_touchdowns_Rsh" bigint,
    "Offense_touchdowns_Rec" bigint,
    "Offense_touchdowns_Def" bigint,
    "Offense_scoring_Rk" bigint,
    "Offense_scoring_INT" bigint,
    "Offense_scoring_FUM" bigint,
    "Offense_scoring_Blk_FG" bigint,
    "Offense_scoring_Blk_Pnt" bigint,
    "Offense_scoring_SFTY" bigint,
    "Offense_scoring_2-PT" bigint,
    "Offense_rushing_Rk" bigint,
    "Offense_rushing_Att" bigint,
    "Offense_rushing_Att/G" bigint,
    "Offense_rushing_Yds" bigint,
    "Offense_rushing_Avg" bigint,
    "Offense_rushing_Yds/G" bigint,
    "Offense_rushing_Lng" bigint,
    "Offense_rushing_Lng_T" bigint,
    "Offense_rushing_1st" bigint,
    "Offense_rushing_1stpct" double precision,
    "Offense_rushing_20+" bigint,
    "Offense_rushing_40+" bigint,
    "Offense_rushing_FUM" bigint,
    "Offense_receiving_Rk" bigint,
    "Offense_receiving_Yds" bigint,
    "Offense_receiving_FUM" bigint,
    "Offense_punting_Rk" bigint,
    "Offense_punting_Punts" bigint,
    "Offense_punting_Yds" bigint,
    "Offense_punting_Net_Yds" bigint,
    "Offense_punting_Lng" bigint,
    "Offense_punting_Lng_T" bigint,
    "Offense_punting_Avg" double precision,
    "Offense_punting_Net_Avg" double precision,
    "Offense_punting_Blk" bigint,
    "Offense_punting_OOB" bigint,
    "Offense_punting_Dn" bigint,
    "Offense_punting_IN_20" bigint,
    "Offense_punting_TB" bigint,
    "Offense_punting_FC" bigint,
    "Offense_punting_Ret" bigint,
    "Offense_punting_RetY" bigint,
    "Offense_punting_TD" bigint,
    "Offense_passing_Rk" bigint,
    "Offense_passing_Comp" bigint,
    "Offense_passing_Att" bigint,
    "Offense_passing_Pct" double precision,
    "Offense_passing_Att/G" double precision,
    "Offense_passing_Yds" bigint,
    "Offense_passing_Avg" bigint,
    "Offense_passing_Yds/G" double precision,
    "Offense_passing_Int" bigint,
    "Offense_passing_1st" bigint,
    "Offense_passing_1stpct" double precision,
    "Offense_passing_Lng" bigint,
    "Offense_passing_Lng_T" bigint,
    "Offense_passing_20+" bigint,
    "Offense_passing_40+" bigint,
    "Offense_passing_Sck" bigint,
    "Offense_passing_Rate" double precision,
    "Offense_offensive_line_Rk" bigint,
    "Offense_offensive_line_Exp" bigint,
    "Offense_offensive_line_rush_left_1st_downs" bigint,
    "Offense_offensive_line_rush_left_stuff" bigint,
    "Offense_offensive_line_rush_left_+10Y" bigint,
    "Offense_offensive_line_rush_left_Pwr" bigint,
    "Offense_offensive_line_rush_center_1st_downs" bigint,
    "Offense_offensive_line_rush_center_stuff" bigint,
    "Offense_offensive_line_rush_center_+10Y" bigint,
    "Offense_offensive_line_rush_center_Pwr" bigint,
    "Offense_offensive_line_rush_right_1st_downs" bigint,
    "Offense_offensive_line_rush_right_stuff" bigint,
    "Offense_offensive_line_rush_right_+10Y" bigint,
    "Offense_offensive_line_rush_right_Pwr" bigint,
    "Offense_offensive_line_Sacks" bigint,
    "Offense_offensive_line_QB_Hits" bigint,
    "Offense_kick_returns_Rk" bigint,
    "Offense_kick_returns" bigint,
    "Offense_kick_returns_Yds" bigint,
    "Offense_kick_returns_Yds_Avg" double precision,
    "Offense_kick_returns_Lng" bigint,
    "Offense_kick_returns_Lng_T" bigint,
    "Offense_kick_returns_TD" bigint,
    "Offense_kick_returns_20+" bigint,
    "Offense_kick_returns_40+" bigint,
    "Offense_kick_returns_FC" bigint,
    "Offense_kick_returns_FUM" bigint,
    "Offense_punt_returns" bigint,
    "Offense_punt_returns_Yds" bigint,
    "Offense_punt_returns_Yds_Avg" double precision,
    "Offense_punt_returns_Lng" bigint,
    "Offense_punt_returns_Lng_T" bigint,
    "Offense_punt_returns_TD" bigint,
    "Offense_punt_returns_20+" bigint,
    "Offense_punt_returns_40+" bigint,
    "Offense_punt_returns_FC" bigint,
    "Offense_punt_returns_FUM" bigint,
    "Offense_kicking_Rk" bigint,
    "Offense_kicking_KO" bigint,
    "Offense_kicking_Yds" bigint,
    "Offense_kicking_OOB" bigint,
    "Offense_kicking_Avg" double precision,
    "Offense_kicking_TB" bigint,
    "Offense_kicking_Pct" double precision,
    "Offense_kicking_returns" bigint,
    "Offense_kicking_returns_Avg" double precision,
    "Offense_kicking_TD" bigint,
    "Offense_kicking_OSK" bigint,
    "Offense_kicking_OSKR" bigint,
    "Offense_game_stats_Rk" bigint,
    "Offense_game_stats_G" bigint,
    "Offense_game_stats_Pts/G" double precision,
    "Offense_game_stats_TotPts" integer,
    "Offense_game_stats_Scrm_Plys" bigint,
    "Offense_game_stats_Yds/G" double precision,
    "Offense_game_stats_Yds/P" double precision,
    "Offense_game_stats_1st/G" double precision,
    "Offense_game_stats_3rd_Md" bigint,
    "Offense_game_stats_3rd_Att" bigint,
    "Offense_game_stats_3rd_Pct" bigint,
    "Offense_game_stats_4th_Md" bigint,
    "Offense_game_stats_4th_Att" bigint,
    "Offense_game_stats_4th_Pct" bigint,
    "Offense_game_stats_Pen" bigint,
    "Offense_game_stats_Pen_Yds" bigint,
    "Offense_game_stats_ToP/G" text,
    "Offense_game_stats_FUM" bigint,
    "Offense_game_stats_Lost" bigint,
    "Offense_game_stats_TO" bigint,
    "Offense_field_goals_Rk" bigint,
    "Offense_field_goals_FGM" bigint,
    "Offense_field_goals_FG_Att" bigint,
    "Offense_field_goals_Pct" bigint,
    "Offense_field_goals_Blk" bigint,
    "Offense_field_goals_Lng" bigint,
    "Offense_field_goals_Lng_T" bigint,
    "Offense_field_goals__Attempts_1-19" bigint,
    "Offense_field_goals__Made_1-19" bigint,
    "Offense_field_goals_Pct_1-19" bigint,
    "Offense_field_goals__Attempts_20-29" bigint,
    "Offense_field_goals__Made_20-29" bigint,
    "Offense_field_goals_Pct_20-29" bigint,
    "Offense_field_goals__Attempts_30-39" bigint,
    "Offense_field_goals__Made_30-39" bigint,
    "Offense_field_goals_Pct_30-39" bigint,
    "Offense_field_goals__Attempts_40-49" bigint,
    "Offense_field_goals__Made_40-49" bigint,
    "Offense_field_goals_Pct_40-49" bigint,
    "Offense_field_goals__Attempts_50plus" bigint,
    "Offense_field_goals__Made_50plus" bigint,
    "Offense_field_goals_Pct_50plus" bigint,
    "Offense_field_goals_XPM" bigint,
    "Offense_field_goals_XP_Att" bigint,
    "Offense_field_goals_XP_Pct" bigint,
    "Offense_field_goals_XK_Blk" bigint,
    "Defense_touchdowns_Rk" bigint,
    "Defense_touchdowns_Total" bigint,
    "Defense_touchdowns_Rsh" bigint,
    "Defense_touchdowns_Rec" bigint,
    "Defense_touchdowns_Ret" bigint,
    "Defense_touchdowns_Def" bigint,
    "Defense_tackles_Rk" bigint,
    "Defense_tackles_Comb" bigint,
    "Defense_tackles_Total" bigint,
    "Defense_tackles_Ast" bigint,
    "Defense_tackles_Sck" bigint,
    "Defense_tackles_FF" bigint,
    "Defense_tackles_Rec" bigint,
    "Defense_tackles_TD" bigint,
    "Defense_scoring_Rk" bigint,
    "Defense_scoring_PRet" bigint,
    "Defense_scoring_KRet" bigint,
    "Defense_scoring_INT" bigint,
    "Defense_scoring_FUM" bigint,
    "Defense_scoring_Blk_FG" bigint,
    "Defense_scoring_Blk_Pnt" bigint,
    "Defense_scoring_XPM" bigint,
    "Defense_scoring_FGM" bigint,
    "Defense_scoring_SFTY" bigint,
    "Defense_scoring_2-PT" bigint,
    "Defense_rushing_Rk" bigint,
    "Defense_rushing_Att" bigint,
    "Defense_rushing_Att/G" double precision,
    "Defense_rushing_Yds" bigint,
    "Defense_rushing_Avg" double precision,
    "Defense_rushing_Yds/G" double precision,
    "Defense_rushing_Lng" bigint,
    "Defense_rushing_Lng_T" bigint,
    "Defense_rushing_1st" bigint,
    "Defense_rushing_1stpct" double precision,
    "Defense_rushing_20+" bigint,
    "Defense_rushing_40+" bigint,
    "Defense_rushing_FUM" bigint,
    "Defense_receiving_Rk" bigint,
    "Defense_receiving_Yds" bigint,
    "Defense_receiving_FUM" bigint,
    "Defense_passing_Rk" bigint,
    "Defense_passing_Comp" bigint,
    "Defense_passing_Att" bigint,
    "Defense_passing_Pct" double precision,
    "Defense_passing_Att/G" double precision,
    "Defense_passing_Yds" bigint,
    "Defense_passing_Avg" double precision,
    "Defense_passing_Yds/G" double precision,
    "Defense_passing_Int" bigint,
    "Defense_passing_1st" bigint,
    "Defense_passing_1stpct" double precision,
    "Defense_passing_Lng" bigint,
    "Defense_passing_Lng_T" bigint,
    "Defense_passing_20+" bigint,
    "Defense_passing_40+" bigint,
    "Defense_passing_Sck" bigint,
    "Defense_passing_Rate" double precision,
    "Defense_interceptions_Rk" bigint,
    "Defense_interceptions_PDef" bigint,
    "Defense_interceptions_Int" bigint,
    "Defense_interceptions_TDs" bigint,
    "Defense_interceptions_Yds" bigint,
    "Defense_interceptions_Lng" bigint,
    "Defense_interceptions_Lng_T" bigint,
    "Defense_game_stats_Rk" bigint,
    "Defense_game_stats_G" bigint,
    "Defense_game_stats_Pts/G" double precision,
    "Defense_game_stats_TotPts" bigint,
    "Defense_game_stats_Scrm_Plys" bigint,
    "Defense_game_stats_Yds/G" double precision,
    "Defense_game_stats_Yds/P" double precision,
    "Defense_game_stats_1st/G" double precision,
    "Defense_game_stats_3rd_Md" bigint,
    "Defense_game_stats_3rd_Att" bigint,
    "Defense_game_stats_3rd_Pct" bigint,
    "Defense_game_stats_4th_Md" bigint,
    "Defense_game_stats_4th_Att" bigint,
    "Defense_game_stats_4th_Pct" bigint,
    "Defense_game_stats_Pen" bigint,
    "Defense_game_stats_Pen_Yds" bigint,
    "Defense_game_stats_ToP/G" text,
    "Defense_game_stats_FUM" bigint,
    "Defense_game_stats_Lost" bigint
);


ALTER TABLE offense_defense

--
-- TOC entry 284 (class 1259 OID 18033)
-- Name: offense_fieldgoals; Type: TABLE; Schema:
--

CREATE TABLE offense_fieldgoals (
    "Offense_field_goals_Rk" bigint,
    "Offense_field_goals_Team" text,
    "Offense_field_goals_FGM" bigint,
    "Offense_field_goals_FG Att" bigint,
    "Offense_field_goals_Pct" bigint,
    "Offense_field_goals_Blk" bigint,
    "Offense_field_goals_Lng" text,
    "Offense_field_goals_A-M" text,
    "Offense_field_goals_Pct.1" double precision,
    "Offense_field_goals_A-M.1" text,
    "Offense_field_goals_Pct.2" double precision,
    "Offense_field_goals_A-M.2" text,
    "Offense_field_goals_Pct.3" double precision,
    "Offense_field_goals_A-M.3" text,
    "Offense_field_goals_Pct.4" double precision,
    "Offense_field_goals_A-M.4" text,
    "Offense_field_goals_Pct.5" double precision,
    "Offense_field_goals_XPM" bigint,
    "Offense_field_goals_XP Att" bigint,
    "Offense_field_goals_Pct.6" bigint,
    "Offense_field_goals_Blk.1" bigint,
    "Offense_field_goals_Year" bigint
);


ALTER TABLE offense_fieldgoals

--
-- TOC entry 285 (class 1259 OID 18039)
-- Name: offense_game_stats; Type: TABLE; Schema:
--

CREATE TABLE offense_game_stats (
    "Offense_game_stats_Rk" bigint,
    "Offense_game_stats_Team" text,
    "Offense_game_stats_G" bigint,
    "Offense_game_stats_Pts/G" double precision,
    "Offense_game_stats_TotPts" double precision,
    "Offense_game_stats_Scrm Plys" text,
    "Offense_game_stats_Yds/G" double precision,
    "Offense_game_stats_Yds/P" double precision,
    "Offense_game_stats_1st/G" double precision,
    "Offense_game_stats_3rd Md" text,
    "Offense_game_stats_3rd Att" text,
    "Offense_game_stats_3rd Pct" bigint,
    "Offense_game_stats_4th Md" text,
    "Offense_game_stats_4th Att" text,
    "Offense_game_stats_4th Pct" bigint,
    "Offense_game_stats_Pen" text,
    "Offense_game_stats_Pen Yds" text,
    "Offense_game_stats_ToP/G" text,
    "Offense_game_stats_FUM" text,
    "Offense_game_stats_Lost" text,
    "Offense_game_stats_TO" text,
    "Offense_game_stats_Year" bigint
);


ALTER TABLE offense_game_stats

--
-- TOC entry 287 (class 1259 OID 18051)
-- Name: offense_kickreturns; Type: TABLE; Schema:
--

CREATE TABLE offense_kickreturns (
    "Offense_kick_returns_Rk" bigint,
    "Offense_kick_returns_Team" text,
    "Offense_kick_returns_Ret" bigint,
    "Offense_kick_returns_Yds" text,
    "Offense_kick_returns_Avg" double precision,
    "Offense_kick_returns_Lng" text,
    "Offense_kick_returns_TD" bigint,
    "Offense_kick_returns_20+" text,
    "Offense_kick_returns_40+" text,
    "Offense_kick_returns_FC" bigint,
    "Offense_kick_returns_FUM" text,
    "Offense_kick_returns_Ret.1" bigint,
    "Offense_kick_returns_RetY" bigint,
    "Offense_kick_returns_Avg.1" double precision,
    "Offense_kick_returns_Lng.1" text,
    "Offense_kick_returns_TD.1" bigint,
    "Offense_kick_returns_20+.1" text,
    "Offense_kick_returns_40+.1" text,
    "Offense_kick_returns_FC.1" bigint,
    "Offense_kick_returns_FUM.1" text,
    "Offense_kick_returns_Year" bigint
);


ALTER TABLE offense_kickreturns

--
-- TOC entry 286 (class 1259 OID 18045)
-- Name: offense_kicks; Type: TABLE; Schema:
--

CREATE TABLE offense_kicks (
    "Offense_kicking_Rk" bigint,
    "Offense_kicking_Team" text,
    "Offense_kicking_KO" bigint,
    "Offense_kicking_Yds" text,
    "Offense_kicking_OOB" bigint,
    "Offense_kicking_Avg" double precision,
    "Offense_kicking_TB" bigint,
    "Offense_kicking_Pct" double precision,
    "Offense_kicking_Ret" bigint,
    "Offense_kicking_Avg.1" text,
    "Offense_kicking_TD" bigint,
    "Offense_kicking_OSK" bigint,
    "Offense_kicking_OSKR" bigint,
    "Offense_kicking_Year" bigint
);


ALTER TABLE offense_kicks

--
-- TOC entry 288 (class 1259 OID 18057)
-- Name: offense_line; Type: TABLE; Schema:
--

CREATE TABLE offense_line (
    "Offense_offensive_line_Rk" bigint,
    "Offense_offensive_line_Team" text,
    "Offense_offensive_line_Exp" bigint,
    "Offense_offensive_line_1st" bigint,
    "Offense_offensive_line_Neg" bigint,
    "Offense_offensive_line_+10Y" bigint,
    "Offense_offensive_line_Pwr" bigint,
    "Offense_offensive_line_1st.1" bigint,
    "Offense_offensive_line_Neg.1" bigint,
    "Offense_offensive_line_+10Y.1" bigint,
    "Offense_offensive_line_Pwr.1" bigint,
    "Offense_offensive_line_1st.2" bigint,
    "Offense_offensive_line_Neg.2" bigint,
    "Offense_offensive_line_+10Y.2" bigint,
    "Offense_offensive_line_Pwr.2" bigint,
    "Offense_offensive_line_Sacks" bigint,
    "Offense_offensive_line_QB Hits" bigint,
    "Offense_offensive_line_Year" bigint
);


ALTER TABLE offense_line

--
-- TOC entry 289 (class 1259 OID 18063)
-- Name: offense_passing; Type: TABLE; Schema:
--

CREATE TABLE offense_passing (
    "Offense_passing_Rk" bigint,
    "Offense_passing_Team" text,
    "Offense_passing_Comp" bigint,
    "Offense_passing_Att" bigint,
    "Offense_passing_Pct" double precision,
    "Offense_passing_Att/G" double precision,
    "Offense_passing_Yds" text,
    "Offense_passing_Avg" double precision,
    "Offense_passing_Yds/G" double precision,
    "Offense_passing_Int" bigint,
    "Offense_passing_1st" bigint,
    "Offense_passing_1stpct" double precision,
    "Offense_passing_Lng" text,
    "Offense_passing_20+" bigint,
    "Offense_passing_40+" bigint,
    "Offense_passing_Sck" bigint,
    "Offense_passing_Rate" double precision,
    "Offense_passing_Year" bigint
);


ALTER TABLE offense_passing

--
-- TOC entry 290 (class 1259 OID 18069)
-- Name: offense_punting; Type: TABLE; Schema:
--

CREATE TABLE offense_punting (
    "Offense_punting_Rk" bigint,
    "Offense_punting_Team" text,
    "Offense_punting_Punts" bigint,
    "Offense_punting_Yds" text,
    "Offense_punting_Net Yds" text,
    "Offense_punting_Lng" text,
    "Offense_punting_Avg" double precision,
    "Offense_punting_Net Avg" text,
    "Offense_punting_Blk" bigint,
    "Offense_punting_OOB" text,
    "Offense_punting_Dn" text,
    "Offense_punting_IN 20" text,
    "Offense_punting_TB" text,
    "Offense_punting_FC" text,
    "Offense_punting_Ret" text,
    "Offense_punting_RetY" text,
    "Offense_punting_TD" text,
    "Offense_punting_Year" bigint
);


ALTER TABLE offense_punting

--
-- TOC entry 291 (class 1259 OID 18075)
-- Name: offense_receiving; Type: TABLE; Schema:
--

CREATE TABLE offense_receiving (
    "Offense_receiving_Rk" bigint,
    "Offense_receiving_Team" text,
    "Offense_receiving_Yds" text,
    "Offense_receiving_FUM" text,
    "Offense_receiving_Year" bigint
);


ALTER TABLE offense_receiving

--
-- TOC entry 292 (class 1259 OID 18081)
-- Name: offense_rushing; Type: TABLE; Schema:
--

CREATE TABLE offense_rushing (
    "Offense_receiving_Rk" bigint,
    "Offense_receiving_Team" text,
    "Offense_receiving_Yds" text,
    "Offense_receiving_FUM" text,
    "Offense_receiving_Year" bigint
);


ALTER TABLE offense_rushing

--
-- TOC entry 293 (class 1259 OID 18087)
-- Name: offense_score; Type: TABLE; Schema:
--

CREATE TABLE offense_score (
    "Offense_scoring_Rk" bigint,
    "Offense_scoring_Team" text,
    "Offense_scoring_INT" bigint,
    "Offense_scoring_FUM" bigint,
    "Offense_scoring_Blk FG" bigint,
    "Offense_scoring_Blk Pnt" bigint,
    "Offense_scoring_SFTY" bigint,
    "Offense_scoring_2-PT" text,
    "Offense_scoring_Year" bigint
);


ALTER TABLE offense_score

--
-- TOC entry 294 (class 1259 OID 18093)
-- Name: offense_touch; Type: TABLE; Schema:
--

CREATE TABLE offense_touch (
    "Offense_touchdowns_Rk" bigint,
    "Offense_touchdowns_Team" text,
    "Offense_touchdowns_Total" bigint,
    "Offense_touchdowns_Rsh" bigint,
    "Offense_touchdowns_Rec" bigint,
    "Offense_touchdowns_Def" bigint,
    "Offense_touchdowns_Year" bigint
);


ALTER TABLE offense_touch

--
-- TOC entry 296 (class 1259 OID 18105)
-- Name: superbowl; Type: TABLE; Schema:
--

CREATE TABLE superbowl (
    "Year" bigint,
    "Team" text,
    "Superbowl_Winner" bigint,
    "Superbowl_Loser_Team" text,
    "Superbowl_Loser" bigint
);


ALTER TABLE superbowl

--
-- TOC entry 234 (class 1259 OID 17437)
-- Name: wnba_players; Type: TABLE; Schema:
--

CREATE TABLE wnba_players (
    "Player" text,
    "Tm" text,
    "Pos" text,
    season bigint,
    statistic_name text,
    statistic double precision
);


ALTER TABLE wnba_players

--
-- TOC entry 236 (class 1259 OID 17451)
-- Name: wnba_players_list; Type: TABLE; Schema:
--

CREATE TABLE wnba_players_list (
    "Player" text,
    player_id bigint
);


ALTER TABLE wnba_players_list

--
-- TOC entry 237 (class 1259 OID 17457)
-- Name: wnba_salary; Type: TABLE; Schema:
--

CREATE TABLE wnba_salary (
    index bigint,
    "Team" text,
    "Average Age" double precision,
    "Active Cap" bigint,
    season bigint
);


ALTER TABLE wnba_salary

--
-- TOC entry 235 (class 1259 OID 17445)
-- Name: wnba_team_list; Type: TABLE; Schema:
--

CREATE TABLE wnba_team_list (
    "Team" text,
    team_id bigint
);


ALTER TABLE wnba_team_list

--
-- TOC entry 233 (class 1259 OID 17431)
-- Name: wnba_teams; Type: TABLE; Schema:
--

CREATE TABLE wnba_teams (
    team text,
    season bigint,
    league text,
    sport text,
    gender text,
    statistic_name text,
    statistic double precision
);


ALTER TABLE wnba_teams

--
-- TOC entry 239 (class 1259 OID 17488)
-- Name: wnba_teamsids; Type: TABLE; Schema:
--

CREATE TABLE wnba_teamsids (
    "Tm" text,
    "Team" text,
    team_id bigint
);


ALTER TABLE wnba_teamsids

--
-- TOC entry 256 (class 1259 OID 17730)
-- Name: wncaa_cities; Type: TABLE; Schema:
--

CREATE TABLE wncaa_cities (
    city_id bigint,
    city text,
    state text
);


ALTER TABLE wncaa_cities

--
-- TOC entry 257 (class 1259 OID 17736)
-- Name: wncaa_conference; Type: TABLE; Schema:
--

CREATE TABLE wncaa_conference (
    conf_abbrev text,
    description text
);


ALTER TABLE wncaa_conference

--
-- TOC entry 254 (class 1259 OID 17718)
-- Name: wncaa_events; Type: TABLE; Schema:
--

CREATE TABLE wncaa_events (
    event_id bigint,
    season bigint,
    day bigint,
    winning_teamid bigint,
    losing_teamid bigint,
    winning_fpoints bigint,
    losing_fpoints bigint,
    winningcpoints bigint,
    losingcpoints bigint,
    elapsed_seconds bigint,
    event_teamid bigint,
    event_playerid bigint,
    event_type text,
    event_subtype text,
    x_position bigint,
    y_position bigint,
    area bigint,
    league text,
    gender text,
    sport text
);


ALTER TABLE wncaa_events

--
-- TOC entry 258 (class 1259 OID 17742)
-- Name: wncaa_gamecities; Type: TABLE; Schema:
--

CREATE TABLE wncaa_gamecities (
    season bigint,
    day bigint,
    winning_teamid bigint,
    losing_team_id bigint,
    event_type text,
    city_id bigint
);


ALTER TABLE wncaa_gamecities

--
-- TOC entry 255 (class 1259 OID 17724)
-- Name: wncaa_players; Type: TABLE; Schema:
--

CREATE TABLE wncaa_players (
    player_id bigint,
    last_name text,
    first_name text,
    team_id bigint
);


ALTER TABLE wncaa_players

--
-- TOC entry 260 (class 1259 OID 17754)
-- Name: wncaa_season; Type: TABLE; Schema:
--

CREATE TABLE wncaa_season (
    season bigint,
    day text,
    region_w text,
    region_x text,
    region_y text,
    region_z text
);


ALTER TABLE wncaa_season

--
-- TOC entry 259 (class 1259 OID 17748)
-- Name: wncaa_seasongames; Type: TABLE; Schema:
--

CREATE TABLE wncaa_seasongames (
    season bigint,
    day bigint,
    winning_teamid bigint,
    winning_score bigint,
    losing_teamid bigint,
    losing_score bigint,
    winning_teamlocation text,
    total_overtime_pd bigint,
    winning_fieldgoals bigint,
    win_fieldgoal_attmpt bigint,
    win_3fieldgoals bigint,
    "win_fieldgoal_attmpt.1" bigint,
    win_freethrows bigint,
    win_freethrows_attmpt bigint,
    win_offensiverebounds bigint,
    win_defensiverebounds bigint,
    win_assists bigint,
    win_turnovers bigint,
    win_steals bigint,
    win_blocks bigint,
    win_personalfouls bigint,
    "winning_fieldgoals.1" bigint,
    l_fieldgoal_attmpt bigint,
    l_3fieldgoals bigint,
    "l_fieldgoal_attmpt.1" bigint,
    l_freethrows bigint,
    l_freethrows_attmpt bigint,
    l_offensiverebounds bigint,
    l_defensiverebounds bigint,
    l_assists bigint,
    l_turnovers bigint,
    l_steals bigint,
    l_blocks bigint,
    l_personalfouls bigint
);


ALTER TABLE wncaa_seasongames

--
-- TOC entry 261 (class 1259 OID 17760)
-- Name: wncaa_teamconference; Type: TABLE; Schema:
--

CREATE TABLE wncaa_teamconference (
    season bigint,
    team_id bigint,
    conf_abbrev text
);


ALTER TABLE wncaa_teamconference

--
-- TOC entry 262 (class 1259 OID 17766)
-- Name: wncaa_teams; Type: TABLE; Schema:
--

CREATE TABLE wncaa_teams (
    team_id bigint,
    team_name text
);


ALTER TABLE wncaa_teams

--
-- TOC entry 263 (class 1259 OID 17772)
-- Name: wncaa_tournament; Type: TABLE; Schema:
--

CREATE TABLE wncaa_tournament (
    season bigint,
    day bigint,
    winning_teamid bigint,
    winning_score bigint,
    losing_teamid bigint,
    losing_score bigint,
    winning_teamlocation text,
    total_overtime_pd bigint,
    winning_fieldgoals bigint,
    win_fieldgoal_attmpt bigint,
    win_3fieldgoals bigint,
    "win_fieldgoal_attmpt.1" bigint,
    win_freethrows bigint,
    win_freethrows_attmpt bigint,
    win_offensiverebounds bigint,
    win_defensiverebounds bigint,
    win_assists bigint,
    win_turnovers bigint,
    win_steals bigint,
    win_blocks bigint,
    win_personalfouls bigint,
    "winning_fieldgoals.1" bigint,
    l_fieldgoal_attmpt bigint,
    l_3fieldgoals bigint,
    "l_fieldgoal_attmpt.1" bigint,
    l_freethrows bigint,
    l_freethrows_attmpt bigint,
    l_offensiverebounds bigint,
    l_defensiverebounds bigint,
    l_assists bigint,
    l_turnovers bigint,
    l_steals bigint,
    l_blocks bigint,
    l_personalfouls bigint
);


ALTER TABLE wncaa_tournament

--
-- TOC entry 224 (class 1259 OID 17098)
-- Name: women_player_; Type: TABLE; Schema:
--

CREATE TABLE women_player_ (
    person_id bigint,
    player text,
    nation text,
    pos text,
    name_other text
);


ALTER TABLE women_player_

--
-- TOC entry 222 (class 1259 OID 17086)
-- Name: women_soccer_fieldplayer; Type: TABLE; Schema:
--

CREATE TABLE women_soccer_fieldplayer (
    person_id bigint,
    season bigint,
    nation text,
    pos text,
    team_id text,
    mp bigint,
    starts bigint,
    min double precision,
    gls bigint,
    ast double precision,
    pk double precision,
    p_katt double precision,
    crd_y bigint,
    crd_r bigint
);


ALTER TABLE women_soccer_fieldplayer

--
-- TOC entry 223 (class 1259 OID 17092)
-- Name: women_soccer_goals; Type: TABLE; Schema:
--

CREATE TABLE women_soccer_goals (
    person_id bigint,
    season bigint,
    nation text,
    pos text,
    team_id text,
    mp bigint,
    starts bigint,
    min bigint,
    ga bigint,
    ga_90 double precision,
    so_ta double precision,
    saves double precision,
    save_pct double precision,
    w bigint,
    d bigint,
    l bigint,
    cs bigint,
    cs_pct double precision,
    crd_y double precision,
    crd_r double precision
);


ALTER TABLE women_soccer_goals

--
-- TOC entry 221 (class 1259 OID 17080)
-- Name: women_soccer_stadium; Type: TABLE; Schema:
--

CREATE TABLE women_soccer_stadium (
    team_id text,
    pri_stadium_name text,
    pri_stadium_alias text,
    pri_town text,
    pri_state text,
    pri_capacity bigint,
    sec_stadium_name text,
    sec_stadium_alias text,
    sec_town text,
    sec_state text,
    sec_capacity double precision,
    avg_attendance bigint,
    season bigint
);


ALTER TABLE women_soccer_stadium

--
-- TOC entry 226 (class 1259 OID 17110)
-- Name: women_soccer_teams; Type: TABLE; Schema:
--

CREATE TABLE women_soccer_teams (
    game_id text,
    season double precision,
    status double precision,
    team_id double precision,
    total_through_ball double precision,
    duel_lost double precision,
    blocked_scoring_att double precision,
    leftside_pass double precision,
    poss_won_att_3_rd double precision,
    dispossessed double precision,
    accurate_keeper_sweeper double precision,
    accurate_cross double precision,
    att_rf_total double precision,
    att_bx_right double precision,
    six_yard_block double precision,
    accurate_pass double precision,
    won_tackle double precision,
    att_assist_setplay double precision,
    att_goal_high_centre double precision,
    att_miss_left double precision,
    total_final_third_passes double precision,
    rightside_pass double precision,
    attempts_conceded_ibox double precision,
    touches double precision,
    total_fwd_zone_pass double precision,
    att_assist_openplay double precision,
    won_contest double precision,
    goals_openplay double precision,
    accurate_fwd_zone_pass double precision,
    total_chipped_pass double precision,
    lost_corners double precision,
    fouled_final_third double precision,
    saves double precision,
    ontarget_scoring_att double precision,
    total_scoring_att double precision,
    blocked_pass double precision,
    attempts_conceded_obox double precision,
    ball_recovery double precision,
    subs_made double precision,
    att_ibox_post double precision,
    poss_won_def_3_rd double precision,
    accurate_back_zone_pass double precision,
    att_cmiss_left double precision,
    att_goal_low_centre double precision,
    goal_assist_openplay double precision,
    passes_right double precision,
    total_throws double precision,
    att_obox_target double precision,
    successful_open_play_pass double precision,
    goal_assist_setplay double precision,
    total_back_zone_pass double precision,
    total_long_balls double precision,
    att_hd_goal double precision,
    accurate_keeper_throws double precision,
    att_obx_centre double precision,
    att_openplay double precision,
    poss_won_mid_3_rd double precision,
    put_through double precision,
    big_chance_created double precision,
    att_ibox_target double precision,
    freekick_cross double precision,
    att_freekick_total double precision,
    goal_kicks double precision,
    att_lf_total double precision,
    open_play_pass double precision,
    goal_assist_intentional double precision,
    aerial_won double precision,
    goal_assist double precision,
    total_pass double precision,
    midfielder_goals double precision,
    total_launches double precision,
    fwd_pass double precision,
    effective_blocked_cross double precision,
    outfielder_block double precision,
    att_miss_high_left double precision,
    goals double precision,
    touches_in_opp_box double precision,
    total_corners_intobox double precision,
    blocked_cross double precision,
    att_miss_right double precision,
    att_bx_centre double precision,
    post_scoring_att double precision,
    ontarget_att_assist double precision,
    long_pass_own_to_opp double precision,
    att_ibox_goal double precision,
    accurate_chipped_pass double precision,
    duel_won double precision,
    total_keeper_sweeper double precision,
    successful_final_third_passes double precision,
    att_rf_goal double precision,
    shield_ball_oop double precision,
    fk_foul_won double precision,
    total_cross_nocorner double precision,
    keeper_throws double precision,
    att_bx_left double precision,
    successful_put_through double precision,
    total_tackle double precision,
    att_sv_low_left double precision,
    passes_left double precision,
    big_chance_scored double precision,
    att_rf_target double precision,
    att_cmiss_high_left double precision,
    accurate_launches double precision,
    poss_lost_all double precision,
    att_sv_low_centre double precision,
    accurate_long_balls double precision,
    challenge_lost double precision,
    total_cross double precision,
    att_goal_low_right double precision,
    clean_sheet double precision,
    att_obox_blocked double precision,
    att_ibox_miss double precision,
    accurate_goal_kicks double precision,
    saved_obox double precision,
    unsuccessful_touch double precision,
    shot_off_target double precision,
    forward_goals double precision,
    poss_lost_ctrl double precision,
    hand_ball double precision,
    goal_assist_deadball double precision,
    att_ibox_blocked double precision,
    aerial_lost double precision,
    att_sv_low_right double precision,
    crosses_18_yard double precision,
    final_third_entries double precision,
    att_hd_total double precision,
    accurate_cross_nocorner double precision,
    effective_clearance double precision,
    fk_foul_lost double precision,
    att_hd_miss double precision,
    won_corners double precision,
    possession_percentage double precision,
    interception double precision,
    attempted_tackle_foul double precision,
    backward_pass double precision,
    first_half_goals double precision,
    interception_won double precision,
    pen_area_entries double precision,
    att_lf_goal double precision,
    accurate_throws double precision,
    big_chance_missed double precision,
    accurate_freekick_cross double precision,
    att_hd_target double precision,
    total_contest double precision,
    hit_woodwork double precision,
    total_clearance double precision,
    long_pass_own_to_opp_success double precision,
    accurate_corners_intobox double precision,
    total_att_assist double precision,
    att_post_left double precision,
    att_setpiece double precision,
    offtarget_att_assist double precision,
    att_obox_miss double precision,
    corner_taken double precision,
    crosses_18_yardplus double precision,
    formation_used double precision,
    total_shots double precision,
    passing_accuracy double precision,
    shot_faced double precision,
    shots_on_goal double precision,
    total_flick_on double precision,
    diving_save double precision,
    att_freekick_miss double precision,
    goals_conceded double precision,
    att_lg_centre double precision,
    total_high_claim double precision,
    error_lead_to_goal double precision,
    goals_conceded_ibox double precision,
    interceptions_in_box double precision,
    total_offside double precision,
    good_high_claim double precision,
    saved_ibox double precision,
    att_miss_high double precision,
    att_sv_high_centre double precision,
    effective_head_clearance double precision,
    accurate_flick_on double precision,
    accurate_layoffs double precision,
    total_yellow_card double precision,
    head_clearance double precision,
    att_lf_target double precision,
    att_cmiss_right double precision,
    att_sv_high_left double precision,
    att_freekick_target double precision,
    overrun double precision,
    total_layoffs double precision,
    total_pull_back double precision,
    att_miss_high_right double precision,
    accurate_through_ball double precision,
    clearance_off_line double precision,
    att_post_high double precision,
    att_cmiss_high double precision,
    att_goal_low_left double precision,
    att_sv_high_right double precision,
    att_obxd_right double precision,
    pts_gained_losing_pos double precision,
    att_cmiss_high_right double precision,
    goals_conceded_obox double precision,
    att_obox_goal double precision,
    pts_dropped_winning_pos double precision,
    error_lead_to_shot double precision,
    att_goal_high_right double precision,
    penalty_conceded double precision,
    penalty_faced double precision,
    att_obx_right double precision,
    pen_goals_conceded double precision,
    att_pen_goal double precision,
    att_goal_high_left double precision,
    penalty_won double precision,
    punches double precision,
    own_goal_accrued double precision,
    att_ibox_own_goal double precision,
    own_goals double precision,
    att_obox_post double precision,
    second_yellow double precision,
    total_red_card double precision,
    defender_goals double precision,
    att_one_on_one double precision,
    att_freekick_post double precision,
    att_pen_post double precision,
    att_post_right double precision,
    contentious_decision double precision,
    att_obxd_left double precision,
    att_hd_post double precision,
    foul_throw_in double precision,
    att_lg_left double precision,
    att_fastbreak double precision,
    shot_fastbreak double precision,
    total_fastbreak double precision,
    att_obx_left double precision,
    accurate_pull_back double precision,
    att_freekick_goal double precision,
    last_man_tackle double precision,
    attempts_obox double precision,
    attempts_ibox double precision,
    att_pen_miss double precision,
    goal_fastbreak double precision,
    att_obp_goal double precision,
    penalty_save double precision,
    att_pen_target double precision,
    att_lg_right double precision,
    att_corner double precision,
    league text,
    sport text,
    gender text
);


ALTER TABLE women_soccer_teams

--
-- TOC entry 240 (class 1259 OID 17599)
-- Name: women_tennis_matches; Type: TABLE; Schema:
--

CREATE TABLE women_tennis_matches (
    tourney_id text,
    tourney_name text,
    surface text,
    draw_size bigint,
    tourney_level text,
    tourney_date bigint,
    match_num bigint,
    winner_id bigint,
    winner_seed text,
    winner_entry text,
    winner_name text,
    winner_hand text,
    winner_ht double precision,
    winner_ioc text,
    winner_age double precision,
    loser_id bigint,
    loser_seed text,
    loser_entry text,
    loser_name text,
    loser_hand text,
    loser_ht double precision,
    loser_ioc text,
    loser_age double precision,
    score text,
    best_of bigint,
    round text,
    minutes double precision,
    w_ace double precision,
    w_df double precision,
    w_svpt double precision,
    "w_1stIn" double precision,
    "w_1stWon" double precision,
    "w_2ndWon" double precision,
    "w_SvGms" double precision,
    "w_bpSaved" double precision,
    "w_bpFaced" double precision,
    l_ace double precision,
    l_df double precision,
    l_svpt double precision,
    "l_1stIn" double precision,
    "l_1stWon" double precision,
    "l_2ndWon" double precision,
    "l_SvGms" double precision,
    "l_bpSaved" double precision,
    "l_bpFaced" double precision,
    winner_rank double precision,
    winner_rank_points double precision,
    loser_rank double precision,
    loser_rank_points double precision,
    league text,
    sport text,
    gender text
);


ALTER TABLE women_tennis_matches

--
-- TOC entry 241 (class 1259 OID 17605)
-- Name: women_tennis_players; Type: TABLE; Schema:
--

CREATE TABLE women_tennis_players (
    player_id bigint,
    first_name text,
    last_name text,
    hand text,
    birth_date double precision,
    country_code text
);


ALTER TABLE women_tennis_players

--
-- TOC entry 225 (class 1259 OID 17104)
-- Name: wommen_soccer_games; Type: TABLE; Schema:
--

CREATE TABLE wommen_soccer_games (
    game_id text,
    game_date text,
    home_team text,
    away_team text,
    home_pts bigint,
    away_pts bigint,
    winner text,
    season bigint
);


ALTER TABLE wommen_soccer_games

--
-- TOC entry 4280 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA  Type: ACL; Schema: -;
--

REVOKE ALL ON SCHEMA FROM rdsadmin;
REVOKE ALL ON SCHEMA FROM PUBLIC;
GRANT ALL ON SCHEMA TO;
GRANT ALL ON SCHEMA TO PUBLIC;


-- Completed on 2020-06-24 11:53:19 EDT

--
-- PostgreSQL database dump complete
--

