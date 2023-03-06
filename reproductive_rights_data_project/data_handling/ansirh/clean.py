"""
Clean ANSIRH data to be munged.
"""

import re
from math import isnan
from reproductive_rights_data_project.util.constants import (
    FILTERED_CHARACTERS_REGEX,
    TYPE_DEFAULTS,
)


def clean(rows):
    """
    Cleans rows of data for universality and useability.

    Author(s): Kate Habich, Chanteria Milner

    Inputs:
        rows (list): list of row dictionaries to clean

    Returns (list):
        List of cleaned ANSIRH row dictionaries.
    """

    # instantiate
    clean_row_list = []
    default_col_types = set_default_types(rows)
    zipcode_len = 5

    for row in rows:
        # set certain floats to str of standard format
        zipcode = str(row["zip code"]).split(".", maxsplit=1)[0]

        if len(zipcode) < zipcode_len:
            num_zeros = zipcode_len - len(zipcode)
            zipcode = "0" * num_zeros + zipcode

        clean_row = {
            "zip code": zipcode,
            "facility ID": str(row["facility ID"]),
        }

        for col_name, value in row.items():
            # set correct default types
            if not value or (not isinstance(value, str) and isnan(value)):
                clean_row[col_name] = default_col_types[col_name]

            # clean strings, convert some to bool
            elif isinstance(value, str):
                value = value.strip('"').strip().lower()
                if value == "yes":
                    clean_row[col_name] = True
                elif value == "no":
                    clean_row[col_name] = False
                else:
                    clean_row[col_name] = value

            elif col_name not in clean_row:
                clean_row[col_name] = value

        clean_row_list.append(clean_row)

    return clean_row_list


def set_default_types(rows):
    """
    Finds the data type of each column in each row and assigns default values
    to those policy entries.

    Author(s): Kate Habich, Chanteria Milner

    Inputs:
        rows (list): list of dictionaries containing healthcare clinic
            information

    Returns(dict):
        Default type associated with column keyed to name of column.
    """

    keys_and_defaults = {}

    for row in rows:
        for k, v in [r for r in row.items() if r not in keys_and_defaults]:
            key = re.sub(FILTERED_CHARACTERS_REGEX, "", str(type(v))).split()[
                -1
            ]
            keys_and_defaults[k] = TYPE_DEFAULTS[key]

    return keys_and_defaults
