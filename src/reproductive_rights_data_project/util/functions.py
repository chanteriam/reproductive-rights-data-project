"""
Creates functions for multiple use across files.
"""
import json
import pandas as pd
from src.reproductive_rights_data_project.util.constants import (
    STANDARD_ENCODING,
)


def to_json(data, file_names):
    """
    Dumps data to json file(s).

    Author(s): Chanteria Milner, Michael Plunkett

    Inputs:
        data (dict): list of dictionaries to output to JSON
        file_names (list): list of file names to export to
    """

    assert len(data) == len(
        file_names
    ), "Incorrect number of data dictionaries passed"

    for i, file_name in enumerate(file_names):
        with open(file_name, "w", encoding=STANDARD_ENCODING) as f:
            json.dump(data[i], f, indent=1)


def translate_code_to_state(state_abr):
    """
    Turns two-letter state code into the full state name.

    Author(s): Kate Habich

    Inputs:
        state_abr (str): two letter state abbreviation

    Returns (str):
        Full state name.
    """
    # TODO: Will refactor with csv in the near future
    # Read in state abbreviation data
    file_name = "./data/state_abbreviations.csv"
    state = pd.read_csv(file_name)

    # Convert to full state name
    state_name = state["state"][state["code"] == state_abr.upper()].values[0]

    return state_name
