'''
Creates functions for multiple use across files.

Author(s): Kate Habich
'''
import pandas as pd 

def translate_code_to_state(state_abr):
    """
    Turns two-letter state code into the full state name.

    Inputs:
        state_abr (str): two letter state abbreviation

    Returns (str):
        Full state name.
    """
    # TODO: Will refactor with csv in the near future
    # Read in state abreviation data
    file_name = "./data/state_abbreviations.csv"
    state = pd.read_csv(file_name)

    # Convert to full state name
    state_name = state["state"][state["code"] == state_abr.upper()].values[0]

    return state_name