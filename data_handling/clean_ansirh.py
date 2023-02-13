"""
Clean ANSIRH data to be munged.

Authors: Kate Habich
"""

import pandas as pd
from .apis.abortion_policy_api import TYPE_DEFAULTS

# TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def clean_data():
    """
    Cleans data for universality and useability.

    Returns (df): dataframe of cleaned ANSIRH data.
    """

    ansirh = read_data().drop(columns="Unnamed: 2")

    complete_ansirh = replace_missing_values(ansirh)

    # TODO: lowercase everything
    # TODO: turn 'yes' to True, 'no' to False

    # return cleaned_data
    pass


def replace_missing_values(data):
    """
    Fill missing values with TYPE_DEFAULT types.
    """

    for col in data.columns:

        # fill NA and NaN values with proper default values for type
        for dtype, _ in TYPE_DEFAULTS.items():
            ### TODO: cant index row of this non-NA column ###
            ### TODO: replace eval() with getattr()
            print(type(data[col][data[col].notnull()][1]))
            if isinstance(type(data[col][data[col].notnull()][0]), eval(dtype)):
                print(f"{col}: {eval(dtype)}")
                data[col].fillna(TYPE_DEFAULTS[dtype])

    pass


def read_data():
    """
    Read ANSIRH csv into a pandas dataframe.

    Returns (df): Pandas dataframe of uncleaned data
    """

    file_name = "./data/AFD_2021_for_ArcGIS_Upload.csv"

    ansirh = pd.read_csv(file_name)

    return ansirh
