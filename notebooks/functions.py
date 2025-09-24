# Add all the imports needed by the functions in the project here
#================================================================
#
#================================================================

# Remember to modify your functions to use the template shown below

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import re

# Standardize column names
def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    return df

# Drop duplicate rows .
def drop_duplicates(df: pd.DataFrame, column) -> pd.DataFrame: 
    return df.drop_duplicates(subset=[column])

# Merge two pandas DataFrames with customizable parameters.
def concat_dataframes(left_df, right_df):
	return pd.concat([left_df,right_df], ignore_index = True)

# Remove all punctuation and all special characters (keeps only letters, numbers, and spaces)
def remove_all_punctuation(df: pd.DataFrame, columns) -> pd.DataFrame:
    df[columns] = df[columns].map(lambda x: re.sub(r'[^A-Za-z0-9 ]+', '', x) if isinstance(x, str) else x)
    return df

# Drop unnecessary columns
def drop_irrelevant_columns(df: pd.DataFrame, columns) -> pd.DataFrame:
    df_drop_cols = df.drop(columns=columns, axis=1, errors="ignore")
    return df_drop_cols

# Filters rows in 'column' of the dataframe that match the provided regex pattern.
def filter_by_regex_pattern(df: pd.DataFrame, column, regex_pattern: str) -> pd.DataFrame:
    df[column] = df[column].lower()
    mask = df[column].str.contains(regex_pattern, flags=re.IGNORECASE, na=False, regex=True)
    return df[mask].copy().reset_index(drop=True)

def standardize_dates(df: pd.DataFrame, column) -> pd.DataFrame:
    # df[column] = pd.to_datetime(df[column], format="%d-%b-%Y", errors='coerce')
    
    # Make a copy of df
    df_merged_dates = df.copy()
    # Convert 'post_until' to datetime (with your format)
    df_merged_dates[column] = pd.to_datetime(df_merged_dates[column], format="%d-%b-%Y", errors='coerce')
    # Format 'post_until' as string in 'dd-mm-YYYY'
    df_merged_dates[column] = df_merged_dates[column].dt.strftime('%d-%m-%Y')
    return df_merged_dates
