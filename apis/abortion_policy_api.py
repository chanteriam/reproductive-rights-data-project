# Dataset courtesy of Abortion Policy API (https://www.abortionpolicyapi.com/)

import requests
import os
import json
import re

APIKEY = os.environ.get("ABORTION_POLICY_API_KEY")
HEADERS = {"token": APIKEY}
TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def main():
    """
    Retrieves API data from abortionpolicyapi.org, cleans dataset, and exports
        cleaned data into .json files.
    """

    # get API data
    policy_areas = get_api_data()

    # fill in missing data
    for state_policies in policy_areas:
        fill_in_missing_data(state_policies)

    # convert dataset to json
    print("Writing out to json file")
    to_json(policy_areas)


def get_api_data():
    """
    Return state policy data for: gestational limits, insurance coverage,
        minors, and waiting periods

    Returns:
        (tuple) tuple of dictionaries for each state and policy type
    """

    # URLS for API data
    gestational_limits_url = (
        "http://api.abortionpolicyapi.com/v1/gestational_limits/states"
    )
    insurance_coverage_url = (
        "http://api.abortionpolicyapi.com/v1/insurance_coverage/states/"
    )
    minors_url = "http://api.abortionpolicyapi.com/v1/minors/states/"
    waiting_periods_url = "http://api.abortionpolicyapi.com/v1/waiting_periods/states/"

    # get API response objects
    r_gestational = requests.get(gestational_limits_url, headers=HEADERS)
    r_insurance = requests.get(insurance_coverage_url, headers=HEADERS)
    r_minors = requests.get(minors_url, headers=HEADERS)
    r_waiting = requests.get(waiting_periods_url, headers=HEADERS)

    # convert response objects to .json
    states_gestational = r_gestational.json()
    states_insurance = r_insurance.json()
    states_minors = r_minors.json()
    states_waiting = r_waiting.json()

    return [states_gestational, states_insurance, states_minors, states_waiting]


def fill_in_missing_data(state_policies):
    """
    Fill in missing characteristics for each state

    Inputs:
        state_policies (dict): dictionary of dictionaries containing abortion
            policies by U.S. states.
    """

    pattern = r'[!.,\'"?:<>]'
    keys_and_defaults = {}

    # get list of states for data cleaning
    states = []

    with open("data/states.txt", "r") as f:
        for state in f:
            states.append(state.strip())

    # set default types for each state policy
    for _, state_info in state_policies.items():
        for k, v in state_info.items():
            if k not in keys_and_defaults.keys():
                key = re.sub(pattern, "", str(type(v))).split()[-1]
                keys_and_defaults[k] = TYPE_DEFAULTS[key]

    # fill in missing data for states currently in the dataset
    for _, state_info in state_policies.items():
        for k, v in keys_and_defaults.items():
            if k not in state_info.keys():
                state_info[k] = v

    # add non-present states with default values
    non_present_states = list(set(states) - set(state_policies.keys()))
    for state in non_present_states:
        state_policies[state] = keys_and_defaults

    # sort dataset by state name
    # code adapted from: https://www.geeksforgeeks.org/python-sort-a-dictionary/
    state_policies = {
        key: val for key, val in sorted(state_policies.items(), key=lambda ele: ele[0])
    }


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

    for i, file in enumerate(file_names):
        with open(file, "w") as f:
            json.dump(policy_areas[i], f, indent=1)
