# Add all the imports needed by the functions in the project here
#================================================================
#
#================================================================

# Remember to modify your functions to use the template shown below

import pandas as pd

'''
def function_name(input1: data_type1, input2: data_type2,..., opt_arg: data_type_opt= default_value) -> output_data_type:
	"""
	Add a description of what the function does

	Arguments:
	---------
	input1: data_type and which information should contain
	input2: data_type and which information should contain
	opt_arg: data_type and which information should contain

	Outputs:
	-------
	data_type and which information will contain
	"""
	
	# Your function code here

	
	return opuput
'''

# Standardize column names
def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    return df


def drop_duplicates(df: pd.DataFrame, column) -> pd.DataFrame: 
    return df.drop_duplicates(subset=[column])
     