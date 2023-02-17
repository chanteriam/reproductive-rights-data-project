"""
Clean ANSIRH data to be munged.

Authors: Kate Habich
"""

import pandas as pd
import re
from apis.abortion_policy_api import TYPE_DEFAULTS

# TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def clean_data():
    """
    Cleans data for universality and useability.

    Returns (df): dataframe of cleaned ANSIRH data.
    """

    ansirh = read_data().drop(columns="Unnamed: 2")

    # replace missing values with correct empty type
    complete_ansirh = replace_missing_values(ansirh)

    # cleanexisting data for continuity and readability
    for col in complete_ansirh.columns:

        print(col, complete_ansirh[col].dtype)
        
        # clean string-type entries
        if complete_ansirh[col].dtype == object:
            complete_ansirh[col].astype("str")

            for row in complete_ansirh[col]:
                if row:
                    print("row:", row)

                    # lowercase everything
                    row.lower().strip('\"')

                    # turn 'yes' to True, 'no' to False
                    ### is this actually going to replace the value?###
                    if row == 'yes':
                        row = True
                    if row == 'no':
                        row = False

        ### TODO: turn zip into strings ###

    return complete_ansirh


def replace_missing_values(data):
    """
    Fill missing values with TYPE_DEFAULT types.
    """

    for col in data.columns:

        # fill NA and NaN values with proper default values for type
        for dtype, _ in TYPE_DEFAULTS.items():
            ### TODO: cant index row of this non-NA column ###
            ### TODO: replace eval() with getattr()
            not_null = data[col][data[col].notnull()]
            # print(type(not_null))
            if isinstance(type(list((data[col])[data[col].notnull()])[0]), eval(dtype)):
                # print(f"{col}: {eval(dtype)}")
                data[col].fillna(TYPE_DEFAULTS[dtype])

    return data


def read_data():
    """
    Read ANSIRH csv into a pandas dataframe.

    Returns (df): Pandas dataframe of uncleaned data
    """

    file_name = "./data/AFD_2021_for_ArcGIS_Upload.csv"

    with open(file_name) as f:
        reader = csv.DictReader(f)

        
    ansirh = pd.read_csv(file_name)

    return ansirh
