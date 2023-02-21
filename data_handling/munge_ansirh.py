"""
Munge ANSIRH data into JSON files binned by state.

Author(s): Kate Habich
"""

import pandas as pd
import json
from .clean_ansirh import clean_ansirh


def main_ansirh():
    """
    Creates state dictionary of data from ANSIRH.

    Returns (None): 
        Writes JSON file with cleaned and formatted ANSIRH data.
    """

    ansirh_data = pd.read_csv("./data/AFD_2021_for_ArcGIS_Upload.csv")

    # drop empty column
    ansirh_data = ansirh_data.drop(["Unnamed: 2"], axis=1)

    # make dictionaries of every row in dataset
    row_dicts = make_row_dicts(ansirh_data)

    # clean data
    clean_row_dicts = clean_ansirh(row_dicts)

    # sort by state
    state_dict = split_by_state(clean_row_dicts)

    # sort by zipcode
    zip_dict = split_by_zip(state_dict)

    # write to JSON
    with open("data/clean_ansirh.json", "w", encoding="utf-8") as outfile:
        json.dump(zip_dict, outfile, indent=1)


def split_by_state(rows):
    """
    Creates dictionary of states containing list of row dictionaries

    Inputs:
        rows (list): list of row dictionaries

    Returns (dict): 
        The state_dict keyed to state containing lists of rows in that state
    """

    state_dict = {}
    for row in rows:

        # translate two letter state code to full name
        full_state = str(translate_code_to_state(row["state"]))

        # create states dictionary with row dicts list as value
        if full_state not in state_dict:
            state_dict[full_state] = [row]
        else:
            state_dict[full_state].append(row)

    return state_dict


def translate_code_to_state(state_abr):
    """
    Turns two-letter state code into the full state name.

    Inputs: 
        state_abr (str): two letter state abbreviation

    Returns (str): full state name

    """

    # read in state abreviation data
    file_name = "./data/state_abbreviations.csv"
    state = pd.read_csv(file_name)

    # convert to full state name
    state_name = state["state"][state["code"] == state_abr.upper()].values[0]

    return state_name


def split_by_zip(state_dict):
    """
    Splits state dictionary by zip.

    Inputs:
        state_dict (dict): dictionary of states with values set to list of
            row dicts

    Returns (dict): 
        The state_dict keyed by zip codes containing lists of rows in that 
        zip code
    """

    complete_dict = {}
    for state, rows in state_dict.items():
        zip_dict = {}
        for row in rows:
            if row["zip code"] not in zip_dict:
                zip_dict[row["zip code"]] = [row]
            else:
                zip_dict[row["zip code"]].append(row)

        # set state value to be dicitonary of zip codes
        # containing list of row dictionaries
        complete_dict[state] = zip_dict

    return complete_dict


def make_row_dicts(data):
    """
    Creates dictionary from column name and information of each row.
    """

    row_dict = data.to_dict("records")

    return row_dict
