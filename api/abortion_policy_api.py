"""
Contains all functions that have to do with fetching data from abortion policy
APIs and saving that data to the `../data` folder.

Author(s): Chanteria Milner, Michael Plunkett
"""

import requests
import os
import json
from util.state_dictionaries import set_default_types, fill_in_missing_data

APIKEY = os.environ.get("ABORTION_POLICY_API_KEY")
HEADERS = {"token": APIKEY}
REQUEST_TIMEOUT = 10

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


def main():
    """
    Retrieves API data from abortionpolicyapi.org, cleans dataset, and exports
        cleaned data into .json files.
    """

    # Get API data
    policy_areas = get_api_data()

    # Fill in missing data
    for state_policies in policy_areas:
        clean(state_policies)

    # Convert dataset to json
    print("Writing out to json file")
    to_json(policy_areas)


def get_api_data():
    """
    Return state policy data for: gestational limits, insurance coverage,
        minors, and waiting periods

    Returns:
        (tuple) tuple of dictionaries for each state and policy type
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
    Fill in missing characteristics for each state.

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.
    """

    # Get list of states for data cleaning
    states = []

    with open("data/states.txt", "r", encoding="utf-8") as f:
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


def to_json(policy_areas):
    """
    Dump state policy data to json file(s)

    Inputs:
        policy_areas (dict): list of dictionaries containing abortion
            policies by U.S. states.
    """

    print("Writing out to json file")
    file_names = [
        "data/abortion_policy_api_gestational.json",
        "data/abortion_policy_api_insurance.json",
        "data/abortion_policy_api_minors.json",
        "data/abortion_policy_api_waiting.json",
    ]

    assert len(policy_areas) == len(
        file_names
    ), "Incorrect number of policy areas passed"

    for i, file_name in enumerate(file_names):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(policy_areas[i], f, indent=1)
