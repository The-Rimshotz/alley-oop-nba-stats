# import libraries
import pandas as pd
import numpy as np
import os

%matplotlib inline 
import matplotlib as plt
import seaborn as sns

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
# import the player_data.csv file into pandas
player_data_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/player_data.csv")

# title and print out shape of dataframe
player_data_shape = player_data_df.shape
print("Player Data Information")
print(f"Consisting of {player_data_shape[0]} rows and {player_data_shape[1]} columns")

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
                                      


# print out the dataframe
player_data_df

#-------- Players DataFrame -------------
# import the Players.csv file into pandas
players_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/Players.csv")
# title and print out shape of dataframe
players_shape = players_df.shape
print("Player Data Information")
print(f"Consisting of {players_shape[0]} rows and {players_shape[1]} columns")
# print out the dataframe
players_df

#-------- Seasons Stats DataFrame -------
# import the Seasons_Stats.csv file into pandas
seasons_stats_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/Seasons_Stats.csv")
# title and print out shape of dataframe
seasons_stats_shape = seasons_stats_df.shape
print("Statistical Information by Season")
print(f"Consisting of {seasons_stats_shape[0]} rows and {seasons_stats_shape[1]} columns")
#print out the dataframe
seasons_stats_df
