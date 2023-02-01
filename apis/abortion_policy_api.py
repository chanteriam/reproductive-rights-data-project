# dataset courtesy of Abortion Policy API (https://www.abortionpolicyapi.com/)

import requests
import os
import json
import re

APIKEY = os.environ.get("ABORTION_POLICY_API_KEY")
HEADERS = {"token": APIKEY}
TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}


def get_states(filepath):
    """
    Transfer .txt of states to a list

    Inputs:
        filepath (string): file path of the states data
    """

    states = []

    with open(filepath, "r") as f:
        for state in f:
            states.append(state.strip())

    return states


def get_api_data():
    """
    Return state policy data for: gestational limits, insurance coverage, minors,
        and waiting periods

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

    r_gestational = requests.get(gestational_limits_url, headers=HEADERS)
    r_insurance = requests.get(insurance_coverage_url, headers=HEADERS)
    r_minors = requests.get(minors_url, headers=HEADERS)
    r_waiting = requests.get(waiting_periods_url, headers=HEADERS)

    states_gestational = r_gestational.json()
    states_insurance = r_insurance.json()
    states_minors = r_minors.json()
    states_waiting = r_waiting.json()

    # Dump to json
    print("Writing out to json file")
    with open("data/abortion_policy_api_gestational_unclean.json", "w") as f:
        json.dump(states_gestational, f, indent=1)

    with open("data/abortion_policy_api_insurance_unclean.json", "w") as f:
        json.dump(states_insurance, f, indent=1)

    with open("data/abortion_policy_api_minors_unclean.json", "w") as f:
        json.dump(states_minors, f, indent=1)

    with open("data/abortion_policy_api_waiting_unclean.json", "w") as f:
        json.dump(states_waiting, f, indent=1)

    return states_gestational, states_insurance, states_minors, states_waiting


def fix_missing_data(state_policies, states):
    """
    Fill in missing characteristics for each state

    Inputs:
        g (list): gestational limit policy by state
        i (list): insurance coverage policy by state
        m (list): minors policy by state
        w (list): waiting periods by state
    """
    pattern = r'[!.,\'"?:<>]'
    keys_and_defaults = {}

    # set default types of each state policy
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


def to_json(g, i, m, w):
    """
    Dump state policy data to json file(s)

    Inputs:
        g (dictionary): gestational limit policy by state
        i (dictionary): insurance coverage policy by state
        m (dictionary): minors policy by state
        w (dictionary): waiting periods by state
    """

    print("Writing out to json file")
    with open("data/abortion_policy_api_gestational.json", "w") as f:
        json.dump(g, f, indent=1)

    with open("data/abortion_policy_api_insurance.json", "w") as f:
        json.dump(i, f, indent=1)

    with open("data/abortion_policy_api_minors.json", "w") as f:
        json.dump(m, f, indent=1)

    with open("data/abortion_policy_api_waiting.json", "w") as f:
        json.dump(w, f, indent=1)


def clean():
    """
    Cleans API dataset by filling in missing values.
    """

    states = get_states("data/states.txt")

    # get API data
    policy_areas = []
    with open("data/abortion_policy_api_gestational_unclean.json", "r") as f:
        policy_areas.append(json.load(f))

    with open("data/abortion_policy_api_insurance_unclean.json", "r") as f:
        policy_areas.append(json.load(f))

    with open("data/abortion_policy_api_minors_unclean.json", "r") as f:
        policy_areas.append(json.load(f))

    with open("data/abortion_policy_api_waiting_unclean.json", "r") as f:
        policy_areas.append(json.load(f))

    # fill in missing data
    for state_policies in policy_areas:
        fix_missing_data(state_policies, states)

    # convert dataset to json
    g, i, m, w = policy_areas
    to_json(g, i, m, w)
