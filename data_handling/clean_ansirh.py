"""
Clean ANSIRH data to be munged.

Authors: Kate Habich
"""

import pandas as pd
import re
import csv
from apis.abortion_policy_api import TYPE_DEFAULTS
from util.state_dictionaries import set_default_types, fill_in_missing_data

# TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def read_data():
    '''
    Reads in ANSIRH data and writes to new file once cleaned.

    Returns: None
        Writes JSON file of cleaned data.
    '''

    file_name = "./data/AFD_2021_for_ArcGIS_Upload.csv"

    with open(file_name) as f:
        reader = csv.DictReader(f)
        writer = csv.DictWriter()

        clean_ansirh(reader)
                    


    def clean_ansirh(reader):
        """
        Cleans data for universality and useability.

        Returns (): dataframe of cleaned ANSIRH data.
        """

        for row in reader:
            for key, value in row.items():
                if key != '':
                    


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


