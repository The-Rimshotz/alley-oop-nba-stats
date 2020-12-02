# Imports
import pandas as pd
import numpy as np
import os
import pprint

import matplotlib as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

import nba_acquire

np.random.seed(123)

#--------- DataFrame Work -----------

#--------- player_data_df -----------
# get it from nba_acquire.py
player_data_df = nba_acquire.player_data()

# change 'name' column to 'player' column so we can merge later
player_data_df = player_data_df.rename(columns={"name" : "player"})

#--------- players_df ---------------
# get it from nba_acquire.py
players_df = nba_acquire.data_of_players()

# change 'Player' column to 'player' so we can merge later
players_df = players_df.rename(columns={"Player" : "player"})

# dropping duplicate column names (the same names as in seasons_stats) so that we can merge in 'final_df'
players_df = players_df.drop(["player", "height", "weight", "college",], axis=1)

#--------- seasons_stats_df ---------
# get it from nba_acquire.py
seasons_stats_df = nba_acquire.seasons_stats()

# get rid of duplicate columns to avoid 'ValueError: Plan shapes are not aligned' error on later df merge
seasons_stats_df = seasons_stats_df.loc[:,~seasons_stats_df.columns.duplicated()]

# converting certain datatypes from floats to integers
convert_dict = {"2_point_tries" : int, 
                "2_pointers" : int,
                "3_point_tries" : int,
                "3_pointers" : int, 
                "age" : int,
                "assists" : int, 
                "blocks" : int, 
                "def_rebounds" : int, 
                "field_goal_attempts" : int, 
                "field_goals" : int,
                "free_throws" : int, 
                "free_throw_attempts" : int, 
                "games" : int, 
                "games_started" : int, 
                "off_rebounds" : int, 
                "personal_fouls" : int, 
                "points" : int, 
                "steals" : int,
                "three_pt_tries" : int,
                "total_rebounds" : int, 
                "turnovers" : int, 
                "year" : int,
               } 

# turn off column limit so I can see the data in all columns:
pd.options.display.max_columns = None
# 
seasons_stats_df = seasons_stats_df.astype(convert_dict) 

#--------- final_df -----------------
def working_df():
    """
    Function to return merged and completely cleaned final_df
    """
    # merging seasons_stats and player_data dfs
    final_df = pd.merge(seasons_stats_df, player_data_df, on=["player"], how="left")

    # merging 'seasons_stats' (w/ 'player_data') and 'players_dfs'
    final_df = pd.concat([final_df, players_df])

    # dropping duplicates for final_df
    final_df.drop_duplicates(subset="player")

    # filling all nulls with 1
    final_df = final_df.fillna(1)

    # changing datatypes of columns for better view

    final_convert = {"2_point_tries" : int, 
                    "2_pointers" : int,
                    "3_point_tries" : int,
                    "3_pointers" : int, 
                    "age" : int,
                    "assists" : int, 
                    "blocks" : int,
                    "born" : int, 
                    "def_rebounds" : int, 
                    "field_goal_attempts" : int, 
                    "field_goals" : int,
                    "free_throws" : int, 
                    "free_throw_attempts" : int, 
                    "games" : int, 
                    "games_started" : int, 
                    "height_inches" : int,
                    "minutes_played" : int, 
                    "off_rebounds" : int, 
                    "personal_fouls" : int, 
                    "points" : int, 
                    "steals" : int,
                    "three_pt_tries" : int,
                    "total_rebounds" : int, 
                    "turnovers" : int,
                    "weight" : int,
                    "year" : int,
                    "year_end" : int, 
                    "year_start" : int,
                } 

    # turn off column limit so I can see the data in all columns:
    pd.options.display.max_columns = None
    
    final_df = final_df.astype(final_convert) 

    # dropping 'position_y', 'born', 'year_start', 'year_end', 'three_pt_tries'
    final_df = final_df.drop(["position_y", "born", "year_start", "year_end", 
                            "three_pt_tries"], axis=1)

    # renaming 'position_x' to just 'position'
    final_df = final_df.rename(columns = {"position_x" : "position"})

    # rearranging columns for reading ease
    final_df = final_df[["player", "position", "age", "height_inches", "weight", "team", 
                        "birth_date", "birth_city", "birth_state", "year", "college", 
                        "games", "games_started", "minutes_played", "usage_%",
                        "points", "field_goals", "field_goal_attempts", 
                        "field_goal_%", "effective_field_goal_%",
                        "2_point_tries", "2_pointers", "2_point_%", 
                        "3_point_tries", "3_pointers", "3_point_%",
                        "free_throws", "free_throw_attempts", "free_throw_%", 
                        "true_shooting_%", "assists", "assist_%", 
                        "blocks", "block_%", "steals", 
                        "steal_%", "total_rebounds", "total_rebound_%", 
                        "off_rebounds", "off_rebound_%", "def_rebounds", "def_rebound_%",
                        "turnovers", "turnover_%", "offensive_win_shares",
                        "defensive_win_shares", "win_shares", "win_shares_per_48min",
                        "personal_fouls", "player_efficiency", "off_box_plus_minus", 
                        "def_box_plus_minus", "box_plus_minus", "value_over_replacement",
                        ]]

    # renaming of more columns for clarity's sake
    final_df = final_df.rename(columns={
        "weight": "weight_lbs", 
        "birth_date" : "date_of_birth",
        "year" : "season",
        "points" : "total_points",
        "field_goals" : "field_goals_made",
        "2_pointers" : "2_pointers_made",
        "2_pointers_tries" : "2_pointers_made",
        "3_pointers" : "3_pointers_made",
        "3_point_tries" : "3_pointers_tried",
        "off_plus_minus" : "value_on_offense", 
        "def_box_plus_minus" : "value_on_defense",
        "def_box_plus_minus" : "total_value", 
        "value_over_replacement" : "value_over_bench_sub"},) 

    # setting 'final_df' column 'player' to index
    final_df = final_df.set_index("player")

    # get the dataframe back
    return final_df