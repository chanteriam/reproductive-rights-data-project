"""
This file works as the central point for running the data_handling package.
"""

import pandas as pd
from data_handling.ansirh.clean import clean_ansirh
from data_handling.ansirh.process import (
    make_row_dicts,
    split_by_state,
    split_by_zip,
    to_json,
)


def main():
    """
    Runs all processes related to data handling.

    Returns (None):
        Writes JSON file with cleaned and formatted application data.
    """
    # TODO: Will refactor with csv in the near future
    ansirh_data = pd.read_csv("./data/AFD_2021_for_ArcGIS_Upload.csv")

    # Drop empty column
    ansirh_data = ansirh_data.drop(["Unnamed: 2"], axis=1)

    # Make dictionaries of every row in dataset
    row_dicts = make_row_dicts(ansirh_data)

    # Clean and sort data
    clean_row_dicts = clean_ansirh(row_dicts)
    state_dict = split_by_state(clean_row_dicts)
    zip_dict = split_by_zip(state_dict)

    # Write to JSON
    to_json(zip_dict, "data/clean_ansirh.json")
