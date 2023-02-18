"""
Munge ANSIRH data into JSON files binned by state.
"""

import pandas as pd
import csv
from .clean_ansirh import clean_data


def main_ansirh():
    """
    Create state dictionary of data from ANSIRH.
    """
    
    ansirh = pd.read_csv("./data/AFD_2021_for_ArcGIS_Upload.csv")

    # drop empty column
    ansirh = ansirh.drop(['Unnamed: 2'], axis=1)

    # make dictionaries of every row in dataset
    row_dicts = make_row_dicts(ansirh)

    # TODO: sort by zipcode
    zip_dict = split_by_zip(row_dicts)

    # TODO: clean data
        # send through shays clean functions
    clean_zip_dict = clean_data(zip_dict)

    # TODO: sort by state

    state_dict = split_by_state(clean_zip_dict)


    return state_dict


def split_by_state(zips):
    '''
    ### NOT DONE ###
    Create dictionary of states containing list of zip dictionaries
    '''

    state_dict = {}
    for zip in zips:
        for row in
        full_state = translate_code_to_state(["state"])
        if not state_dict[full_state]:
            state_list = [row]

        else:
            state_list.append(row)

        state_dict[full_state] = state_list
            
    return state_dict


    # zip_dict = {}
    # for row in rows:
    #     if row["zip code"] not in zip_dict:
    #         zip_dict[row["zip code"]] = [row]

    #     else:
    #         zip_dict[row["zip code"]].append(row)
    
    # return zip_dict


def translate_code_to_state(state_abr):
    '''
    Turns two-letter state code into the full state name.
    '''

    # read in state abreviation data
    file_name = "./data/state_abbreviations.csv"
    state = pd.read_csv(file_name)


    state_name = state["state"][state["code"] == state_abr.upper()]

    return state_name


def split_by_zip(rows):
    '''
    Split state dictionary by zip.

    Inputs:
        rows (list): list of row dictionaries

    Returns (dict): zip dictinary containing lists of rows in that zip
    '''

    zip_dict = {}
    for row in rows:
        if row["zip code"] not in zip_dict:
            zip_dict[row["zip code"]] = [row]

        else:
            zip_dict[row["zip code"]].append(row)
    
    return zip_dict


def make_row_dicts(data):
    '''
    Create dictionary from column name and information of each row.
    '''

    row_dict = data.to_dict('records')

    return row_dict



                    
                    




        