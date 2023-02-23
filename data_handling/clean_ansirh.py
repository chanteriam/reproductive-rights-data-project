"""
Clean ANSIRH data to be munged.

Author(s): Kate Habich, Chanteria Milner
"""

import re
from util.constants import FILTERED_CHARACTERS_REGEX, TYPE_DEFAULTS


def clean_ansirh(rows):
    """
    Cleans rows of data for universality and useability.

    Inputs:
        rows (list): list of row dictionaries to clean

    Returns (list):
        List of cleaned ANSIRH row dictionaries.
    """

    # instantiating
    default_col_types = set_default_types(rows)
    clean_row_list = []

    for row in rows:
        # setting certain floats to str of standard length
        clean_row = {
            "zip code": str(row["zip code"])[:5],
            "facility ID": str(row["facility ID"]),
        }

        for col_name, value in row.items():

            # if nan, set to correct default type
            if not value:
                clean_row[col_name] = default_col_types[col_name]

            # if string type, clean it up
            elif isinstance(value, str):
                value.strip('"').lower()
                if value.lower() == "yes":
                    clean_row[col_name] = True
                elif value.lower() == "no":
                    clean_row[col_name] = False
                else:
                    clean_row[col_name] = value.lower()

            # if no cleaning happens, transfer data over as is
            elif col_name not in clean_row:
                clean_row[col_name] = value

        clean_row_list.append(clean_row)

    return clean_row_list


def set_default_types(rows):
    """
    Finds the data type of each column in each row and assigns default values
    to those policy entries.

    Inputs:
        rows (list): list of dictionaries containing healthcare clinic
            information

    Returns(dict):
        Default type associated with column keyed to name of column.
    """

    pattern = r'[!.,\'"?:<>]'
    keys_and_defaults = {}

    for row in rows:
        for k, v in [r for r in row if r not in keys_and_defaults].items():
            key = re.sub(FILTERED_CHARACTERS_REGEX, "", str(type(v))).split()[
                -1
            ]
            keys_and_defaults[k] = TYPE_DEFAULTS[key]

    return keys_and_defaults
