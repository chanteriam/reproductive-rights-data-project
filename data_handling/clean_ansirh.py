"""
Clean ANSIRH data to be munged.

Authors: Kate Habich
"""

import pandas as pd
import re
import csv
from util.state_dictionaries import TYPE_DEFAULTS
# from apis.abortion_policy_api import TYPE_DEFAULTS
# from util.state_dictionaries import set_default_types, fill_in_missing_data

# TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


# def read_data():
#     '''
#     ### DELETE? ###
#     Reads in ANSIRH data and writes to new file once cleaned and munged.

#     Returns: None
#         Writes JSON file of cleaned data.
#     '''

#     file_name = "./data/AFD_2021_for_ArcGIS_Upload.csv"

#     with open(file_name) as f:
#         reader = csv.DictReader(f)
#         writer = csv.DictWriter()

#         clean_ansirh(reader)
                    

def clean_ansirh(rows):
    """
    Cleans rows of data for universality and useability.

    Inputs:
        rows (list): list of row dictionaries to clean

    Returns (list ): list of cleaned ANSIRH row dictionaries
    """

    # instantiating
    print("cleaning")

    ### may not work well with object types
    default_col_types = set_default_types(rows) # needs to happen after all types are corrected
    clean_row_list = []

    for row in rows:
        clean_row = {}
        # clean by column section

        # setting zip code data type to string of length 5
        clean_row["zip code"] = str(row["zip code"])[:5]
        clean_row["facility ID"] = str(row["facility ID"])
        
        for col_name, value in row.items():

            # if nan, set default type for 
            if not value:
                clean_row[col_name] = default_col_types[col_name]

            # if string type, clean it up
            print(type(value))
            elif type(value) == str or type(value) == object:
                print("string type identified")
                value.strip('\"').lower()
                if value == "yes":
                    clean_row[col_name] = True
                if value == "no":
                    clean_row[col_name] = False
            

            # if no cleaning happens, just transfer data over as is
            elif col_name not in clean_row:
                clean_row[col_name] = value
        

        clean_row_list.append(clean_row)
        
    return clean_row_list


    # # replace missing values with correct empty type
# complete_ansirh = replace_missing_values(ansirh)

# # cleanexisting data for continuity and readability
# for col in complete_ansirh.columns:

#     print(col, complete_ansirh[col].dtype)
    
#     # clean string-type entries
#     if complete_ansirh[col].dtype == object:
#         complete_ansirh[col].astype("str")

#         for row in complete_ansirh[col]:
#             if row:
#                 print("row:", row)

#                 # lowercase everything
#                 row.lower().strip('\"')

#                 # turn 'yes' to True, 'no' to False
#                 ### is this actually going to replace the value?###
#                 if row == 'yes':
#                     row = True
#                 if row == 'no':
#                     row = False

    #     ### TODO: turn zip into strings ###

    # return complete_ansirh


def set_default_types(rows):
    '''
    Finds the data type of each column in each row and assigns default values 
        to those policy entries.
    
    Inputs:
        rows (list): list of dictionaries containing healthcare clinic 
            information
    
    Returns: 
        (dict) name of column and default type associated with column
    '''
    # from shay
    pattern = r'[!.,\'"?:<>]'
    keys_and_defaults = {}

    for row in rows:
        for k, v in row.items():
                if k not in keys_and_defaults.keys():
                    key = re.sub(pattern, "", str(type(v))).split()[-1]
                    keys_and_defaults[k] = TYPE_DEFAULTS[key]

    # print("dafault types:", keys_and_defaults)
    return keys_and_defaults


def fill_missing_data(rows, defaults):
    """
    ### NOT USING? ###
    Fills in missing policy entries for each row in the dataset.

    Inputs:
        rows (list): list of dictionaries containing healthcare clinic 
            information
        defaults (dict): default policy entries and associated values
    """

    # from shay
    for row in rows:
        for k, v in row.items():
            if not v:
                row[k] = defaults[k]
    