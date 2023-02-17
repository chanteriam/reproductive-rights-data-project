"""
Utility functions that have to do with handling state policy dictionaries.

Author(s): Chanteria Milner, Michael Plunkett
"""

import re

TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def set_default_types(state_policies):
    """
    Finds the number and type of policy entries in each state dictionary and
        assigns default values to those policy entries.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.

    Returns:
        (dictionary) name of policy entry and default type associated with entry
    """

    pattern = r'[!.,\'"?:<>]'
    keys_and_defaults = {}

    # Set default types for each state policy
    for _, state_info in state_policies.items():
        for k, v in state_info.items():
            if k not in keys_and_defaults.keys():
                key = re.sub(pattern, "", str(type(v))).split()[-1]
                keys_and_defaults[k] = TYPE_DEFAULTS[key]

    return keys_and_defaults


def fill_in_missing_data(state_policies, defaults):
    """
    Fills in missing policy entries for states currently in the dataset.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.
        defaults (dict): default policy entries and associated values
    """

    # Fill in missing data for states currently in the dataset
    for _, state_info in state_policies.items():
        for k, v in defaults.items():
            if k not in state_info.keys():
                state_info[k] = v
