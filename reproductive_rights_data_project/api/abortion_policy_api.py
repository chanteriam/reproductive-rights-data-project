"""
Contains all functions that have to do with fetching data from abortion policy
APIs and saving that data to the `../data` folder.
"""

import os
import re

import requests

from reproductive_rights_data_project.util.constants import (
    FILE_NAME_ABORTION_POLICY_API_GESTATION,
    FILE_NAME_ABORTION_POLICY_API_INSURANCE,
    FILE_NAME_ABORTION_POLICY_API_MINORS,
    FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
    FILE_NAME_STATE_NAMES,
    FILTERED_CHARACTERS_REGEX,
    REQUEST_TIMEOUT,
    STANDARD_ENCODING,
    TYPE_DEFAULTS,
)
from reproductive_rights_data_project.util.functions import to_json

ABORTION_POLICY_API_KEY = os.environ.get("ABORTION_POLICY_API_KEY")
HEADERS = {"token": ABORTION_POLICY_API_KEY}

# URLs have been made constants for testing purposes
URL_AP_COVERAGE = (
    "https://api.abortionpolicyapi.com/v1/insurance_coverage/states/"
)
URL_AP_GESTATIONAL_LIMITS = (
    "https://api.abortionpolicyapi.com/v1/gestational_limits/states"
)
URL_AP_MINORS = "https://api.abortionpolicyapi.com/v1/minors/states/"
URL_AP_WAITING_PERIODS = (
    "https://api.abortionpolicyapi.com/v1/waiting_periods/states/"
)


def get_and_save_abortion_policy_api_data():
    """
    Retrieves API data from abortionpolicyapi.org, cleans dataset, and exports
    cleaned data into JSON files.
    """

    # Get API data
    policy_areas = get_data()

    # Fill in missing data
    for state_policies in policy_areas:
        clean(state_policies)

    # Convert dataset to json
    file_names = [
        FILE_NAME_ABORTION_POLICY_API_GESTATION,
        FILE_NAME_ABORTION_POLICY_API_INSURANCE,
        FILE_NAME_ABORTION_POLICY_API_MINORS,
        FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
    ]
    to_json(policy_areas, file_names)


def get_data():
    """
    Retrieves state policy data for: gestational limits, insurance coverage,
    minors, and waiting periods

    Returns (list):
        List of dictionaries for each state and policy type.
    """

    # Get API response objects
    r_gestational = requests.get(
        URL_AP_GESTATIONAL_LIMITS, headers=HEADERS, timeout=REQUEST_TIMEOUT
    )
    r_insurance = requests.get(
        URL_AP_COVERAGE, headers=HEADERS, timeout=REQUEST_TIMEOUT
    )
    r_minors = requests.get(
        URL_AP_MINORS, headers=HEADERS, timeout=REQUEST_TIMEOUT
    )
    r_waiting = requests.get(
        URL_AP_WAITING_PERIODS, headers=HEADERS, timeout=REQUEST_TIMEOUT
    )

    # Convert response objects to .json
    states_gestational = r_gestational.json()
    states_insurance = r_insurance.json()
    states_minors = r_minors.json()
    states_waiting = r_waiting.json()

    return [states_gestational, states_insurance, states_minors, states_waiting]


def clean(state_policies):
    """
    Fills in missing characteristics for each state.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.
    """

    # Get list of states for data cleaning
    states = []

    with open(FILE_NAME_STATE_NAMES, "r", encoding=STANDARD_ENCODING) as f:
        for state in f:
            states.append(state.strip())

    # Set default types for each state policy
    policy_defaults = set_default_types(state_policies)

    # Fill in missing data for current states
    fill_in_missing_data(state_policies, policy_defaults)

    # Add states missing in the dataset
    add_missing_states(state_policies, policy_defaults, states)

    # Sort dataset by state name
    state_policies = dict(
        sorted(state_policies.items(), key=lambda ele: ele[0])
    )


def add_missing_states(state_policies, defaults, states):
    """
    Adds missing state entries to the dataset.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.
        defaults (dict): default policy entries and associated values
        states (list): list of total states that should be in dataset
    """

    non_present_states = list(set(states) - set(state_policies.keys()))
    for state in non_present_states:
        state_policies[state] = defaults


def set_default_types(state_policies):
    """
    Finds the number and type of policy entries in each state dictionary and
    assigns default values to those policy entries.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.

    Returns (dict):
        name of policy entry and default type associated with entry
    """

    keys_and_defaults = {}

    # Set default types for each state policy
    for _, state_info in state_policies.items():
        for k, v in state_info.items():
            if k not in keys_and_defaults:
                key = re.sub(
                    FILTERED_CHARACTERS_REGEX, "", str(type(v))
                ).split()[-1]
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
