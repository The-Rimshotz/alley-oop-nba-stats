# import libraries
import pandas as pd
import numpy as np
import os

import matplotlib as plt
import seaborn as sns

np.random.seed(123)

# function to get total null values in each column
def null_counts(df):
    """
    function to count the number of null values in each df column
    """
    missing = df.isna().sum()
    return missing

# function to determine percentage of NaN values in each column:
def null_percentages(df):
    """
    returns the percentage of NaN values in each column to help determine
    whether or not the column in question should be kept or dropped
    """
    perct = ((df.isna().sum()) / len(df) * 100)
    return perct

#------- Player Data DataFrame ------------
def player_data():
    """
    function to return the cleaned player_data_df
    """
    # import the player_data.csv file into pandas
    player_data_df = pd.read_csv("./data/raw/player_data.csv")

    # title and print out shape of dataframe
    a = player_data_df.isnull().sum().sum()
    player_data_shape = player_data_df.shape
    print("Player Data Information")
    print(f"Consisting of {player_data_shape[0]} rows and {player_data_shape[1]} columns")
    print(f"It has loads of data, but also has {a} missing values.")

    # cleaning up missing values for george karl
    player_data_df["height"] = player_data_df["height"].fillna("6-2")
    player_data_df["weight"] = player_data_df["weight"].fillna(185)
    player_data_df["position"] = player_data_df["position"].fillna("G")

    # 9 simple steps to changing heights from 'feet-inches' format
    # 1.) adds column for feet using 'height' column
    player_data_df["feet"] = player_data_df.height.str[:1] 
    # 2.) adds column for inches using 'height' column
    player_data_df["inches"] = player_data_df.height.str[2:4]
    # 3.) converts 'feet' column from string to integer
    player_data_df["feet"] = player_data_df["feet"].astype(int)
    # 4.) converts 'inches' column from string to integer
    player_data_df["inches"] = player_data_df["inches"].astype(int)
    # 5.) converts 'feet' into inches
    player_data_df["feet_in_inches"] = (player_data_df["feet"] * 12).to_frame("feet")
    # 6.) adds new column 'total_inches' that adds the totals from 'feet_in_inches' and 'inches' columns
    player_data_df["total_inches"] = (player_data_df["feet_in_inches"] + player_data_df["inches"])
    # 7.) replaces the original values in 'height' with the new values from 'total_inches'
    player_data_df = player_data_df.assign(height=player_data_df["total_inches"])
    # 8.) drops 'feet,' 'inches,' 'feet_in_inches,' and 'total_inches' columns we used to convert the original data to the new
    player_data_df = player_data_df.drop(["feet", "inches", "feet_in_inches", 
                                        "total_inches"], axis=1)
    # 9.) renames the 'height' column to 'height_inches'
    player_data_df = player_data_df.rename(columns={"height" : "height_inches"})
                                        
    # replaces the 'nan' values in 'college' with 'no college listed'
    player_data_df["college"] = player_data_df["college"].fillna("No college listed")

    # replaces 'nan' values in 'birth_date' column with 'not listed'
    player_data_df["birth_date"] = player_data_df["birth_date"].fillna("Not listed")

    # print out the dataframe
    return player_data_df

#-------- Players DataFrame -------------
def data_of_players():
    """
    function to return cleaned players_df
    """
    # import the Players.csv file into pandas
    players_df = pd.read_csv("../data/raw/Players.csv")
    # title and print out shape of dataframe
    b = players_df.isnull().sum().sum()
    players_shape = players_df.shape
    print("Player Data Information")
    print(f"Consisting of {players_shape[0]} rows and {players_shape[1]} columns")
    print(f"Not all data is present.  We still have {b} missing values.")

    # change the spelling of 'collage' column to 'college'
    players_df = players_df.rename(columns={"collage" : "college"})

    # drop 'Unnamed: 0' column
    players_df = players_df.drop(columns="Unnamed: 0", axis=1)

    # drop index 223 - all values in that row are NaN
    players_df = players_df.drop([223])

    # convert 'height' from centimeters to inches (2.54 cm / inch)
    players_df["height"] = players_df.height.div(2.54).round(decimals=2)
    # get rid of decimal in height
    players_df["height"] = players_df["height"].astype(int)

    # convert 'weight' from kilos to pounds (2.2 lbs / kilo)
    players_df["weight"] = players_df.weight.mul(2.2).round(decimals=2)
    # get rid of decimal point in weight
    players_df["weight"] = players_df["weight"].astype(int)

    # getting rid of that unnecessary '.0' in 'born'
    players_df["born"] = players_df["born"].astype(int)

    # replacing the nan values in 'college', 'birth_city,' and 'birth_state'
    columns = ["college" , "birth_city", "birth_state"]
    players_df[columns] = players_df[columns].fillna("Not Available")

    # print out the dataframe
    return players_df

#-------- Seasons Stats DataFrame -------
def seasons_stats():
    """
    function to return cleaned seasons_stats_df
    """
    # import the Seasons_Stats.csv file into pandas
    seasons_stats_df = pd.read_csv("data/raw/Seasons_Stats.csv")
    # title and print out shape of dataframe
    c = seasons_stats_df.isnull().sum().sum()
    seasons_stats_shape = seasons_stats_df.shape
    print("Statistical Information by Season")
    print(f"Consisting of {seasons_stats_shape[0]} rows and {seasons_stats_shape[1]} columns")
    print(f"While informative, still needs work: we are missing {c} values.")

    # rename the columns for clarity
    seasons_stats_df.rename(
            columns={
                "Year": "year",
                "Player": "player",
                "Pos": "position",
                "Age": "age",
                "Tm": "team",
                "G": "games",
                "GS": "games_started",
                "MP": "minutes_played",
                "PER": "player_efficiency",
                "TS%": "true_shooting_%",
                "3PAr": "three_pt_tries",
                "FTr": "free_throws",
                "ORB%": "off_rebound_%",
                "DRB%": "def_rebound_%",
                "TRB%": "total_rebound_%",
                "AST%": "assist_%",
                "STL%": "steal_%",
                "BLK%": "block_%",
                "TOV%" : "turnover_%",
                "USG%": "usage_%",
                "blanl": "blank1",
                "OWS": "offensive_win_shares",
                "DWS": "defensive_win_shares",
                "WS": "win_shares",
                "WS/48": "win_shares_per_48min",
                "OBPM": "off_box_plus_minus",
                "DBPM": "def_box_plus_minus",
                "BPM": "box_plus_minus",
                "VORP": "value_over_replacement",
                "FG" : "field_goals", 
                "FGA" : "field_goal_attempts",
                "FG%" : "field_goal_%", 
                "3P" : "3_pointers", 
                "3PA" : "3_point_tries",
                "3P%" : "3_point_%",
                "2P" : "2_pointers",
                "2PA" : "2_point_tries",
                "2P%" : "2_point_%",
                "eFG%" : "effective_field_goal_%",
                "FT" : "free_throws",
                "FTA" : "free_throw_attempts",
                "FT%" : "free_throw_%",
                "ORB" : "off_rebounds",
                "DRB" : "def_rebounds",
                "TRB" : "total_rebounds",
                "AST" : "assists",
                "STL" : "steals",
                "BLK" : "blocks",
                "TOV" : "turnovers",
                "PF" : "personal_fouls",
                "PTS" : "points",
            },
            inplace=True,
            )

    # drop 'Unnamed: 0,' 'blank1', and 'blank2'columns
    seasons_stats_df = seasons_stats_df.drop(["Unnamed: 0","blank1", "blank2"], axis=1)

    # replacing NaN ages with 1's
    seasons_stats_df["age"] = seasons_stats_df["age"].fillna(1)

    # dropping rows that are all NaNs
    seasons_stats_df = seasons_stats_df.drop([312,   487,   618,   779,   911,  1021,  1128,  1236,  1348,
                1459,  1577,  1682,  1808,  1942,  2078,  2211,  2347,  2481,
                2659,  2866,  3068,  3314,  3580,  3850,  4096,  4373,  4648,
                5006,  5381,  5726,  6084,  6448,  6822,  7214,  7558,  7921,
                8301,  8680,  9107,  9546, 10006, 10448, 10907, 11357, 11839,
                12292, 12838, 13413, 13961, 14469, 14966, 15504, 16005, 16489,
                17075, 17661, 18225, 18742, 19338, 19921, 20500, 21126, 21678,
                22252, 22864, 23516, 24095])

    # change dtypes from floats to integers in the appropriate columns
    cols = ["year", "age", "games", "assists", "personal_fouls", "points"]
    seasons_stats_df[cols] = seasons_stats_df[cols].astype(int)

    # fill the rest of the nulls with '1' for modeling purposes
    seasons_stats_df = seasons_stats_df.fillna(1)

    # change these newly minted '1's from floats to integers
    more_cols = ["games_started", "minutes_played", "off_rebounds", "def_rebounds",
                "total_rebounds", "steals", "blocks", "turnovers"]
    seasons_stats_df[more_cols] = seasons_stats_df[more_cols].astype(int)

    # get rid of duplicate columns to avoid 'ValueError: Plan shapes are not aligned' error on later df merge
    seasons_stats_df = seasons_stats_df.loc[:,~seasons_stats_df.columns.duplicated()]

    # print out the dataframe
    return seasons_stats_df

#-------- Resources for player_data_df ----------


#1.) Dataset from Kaggle can be found at https://www.kaggle.com/drgilermo/nba-players-stats?select=Players.csv
#2.) George Karl information on his time with the Spurs is at https://www.statscrew.com/basketball/roster/t-SAA/y-1974

#-------- Resources for seasons_stats_df -------
# 1.) Year that they started taking rebound stats: https://en.wikipedia.org/wiki/Rebound_(basketball)#:~:text=Both%20offensive%20and%20defensive%20rebounds,missed%20shots%20will%20likely%20land.

#2.) Year they started taking data on steals: https://en.wikipedia.org/wiki/Steal_(basketball)#:~:text=Steals%20were%20first%20recorded%20in,his%20on%20April%203%2C%201999. 

#3.) Year they started recording blocks: https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_annual_blocks_leaders#:~:text=The%20block%20title%20was%20first,on%20blocks%20were%20first%20compiled.

#4.) Year they started with turnover data: https://en.wikipedia.org/wiki/Turnover_(basketball)#:~:text=Turnovers%20were%20first%20officially%20recorded,during%20the%201967%E2%80%9368%20season.

#5.) Year of ABA-NBA merger: https://www.washingtonpost.com/graphics/sports/nba-aba-merger/#:~:text=In%201976%2C%20four%20ABA%20teams,for%20the%20first%20three%20seasons.