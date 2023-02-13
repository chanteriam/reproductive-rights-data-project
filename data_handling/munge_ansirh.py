"""
Munge ANSIRH data into JSON files binned by state.
"""

import pandas as pd
from .clean_ansirh import clean_data


def main_ansirh():
    """
    Create state dictionary of data from ANSIRH.
    """
    ansirh = clean_data()

    row_dicts = make_row_dict(ansirh)

    # state_dict = split_by_state(ansirh)

    # ### flip this to go from micro --> macro (row to state)
    # for state in state_dict:
    #     zip_dict = split_by_zip(state)

    #     for row in zip_dict:
    #         row_dict = make_row_dict(row)

    # pass


def split_by_state(data):
    '''
    Create dictionary of states matched to a list of tuples of row data
    '''

    state_dict = {}
    for row in data.itertuples():
        full_state = translate_code_to_state(row["state"])
        if not state_dict[full_state]:
            state_list = [row]

        else:
            state_list.append(row)

        state_dict[full_state] = state_list
            
    return state_dict


def translate_code_to_state(state_abr):
    '''
    Turns two-letter state code into the full state name.
    '''

    # read in state abreviation data
    file_name = "./data/state_abbreviations.csv"
    state = pd.read_csv(file_name)

    state_name = state["state"][state["code"] == state_abr.upper()]

    return state_name


def split_by_zip():
    '''
    Split state dictionary by zip.
    '''
    pass


def make_row_dict(data):
    '''
    Create dictionary from column name and information of each row.
    '''

    row_dict = data.to_dict('records')

    return row_dict
