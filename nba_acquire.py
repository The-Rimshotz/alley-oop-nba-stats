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

# import the player_data.csv file into pandas
player_data_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/player_data.csv")
player_data_df

# import the Players.csv file into pandas
players_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/Players.csv")
players_df

# import the Seasons_Stats.csv file into pandas
seasons_stats_df = pd.read_csv("/Users/DataScience/Rimshotz/alley-oop-nba-stats/Seasons_Stats.csv")
seasons_stats_df