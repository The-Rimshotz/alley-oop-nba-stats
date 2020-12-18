######## Nick's Code ###############

# function to see how many nulls are in the columns
def null_counts(df):
    """
    function to count the number of null values in each df column
    """
    missing = df.isna().sum()
    return missing

# function to determine percentage of NaN values in each column
def null_percentages(df):
    """
    returns the percentage of NaN values in each column to help determine
    whether or not the column in question should be kept or dropped
    """
    
    perct = round((df.isna().sum()) / len(df) * 100), 2
    return perct

# function to combine both 'null_counts' and 'null_percentages'
def null_feedback(df):
    """
    function that tells the user the info on the DataFrame's NaNs
    """
    x = null_counts(df)
    y = null_percentages(df)
    print(f"Total number of NaNs by column: \n {x}.")
    print(f"Percentage of columns that are NaN: \n {y}.")
    return 


######### Suggested Modification ###############

def null_tracker(df):
    """
    Takes in a dataframe, returns nothing.
    Prints the overall count of missing values in the data as well as percentages.
    """
    # Returns the total number of missing values in each column
    total_nans = df.isna().sum()
    # Returns the percentage of missing values in each column
    perc_nans = round(df.isna().sum() / len(df) * 100, 2)
    
    # Prints out the results of checking for nulls
    print(f'Total number of missing values in each column.')
    print(total_nans)
    
    print('\n')
    
    print(f'Percentage of missing values within each column')
    print(perc_nans)
    
    # Notes: 
        # One line of code which will be used very sparingly doesn't really need it's own function
        # unless it's being called by itself. I don't have a good rule of thumb, but maybe if it's more
        # than 4 lines and really needs to be commented heavily to explain it then it should be it's own
        # function.
        
        # On the same note of one line functions, it's not necessary to create a variable to hold the result.
        # This is a little bit harder to grasp, but when you return something from a function, that return
        # doesn't have to be a variable containing an expression, it can just be the expression. The return 
        # itself almost acts as a container for the expression. 
        # Case in point, if I wrote a function that just returns if something is true or false, I can just say
        # return 2 == 2, and it would work just as easily if I made a variable called equalsTwo and then 
        # returned it.
        
        # I did like your solution for printing out the null percentages. Won't lie, I forgot how to do that
        # so it was cool to see.