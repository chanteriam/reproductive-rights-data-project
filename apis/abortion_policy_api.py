# dataset courtesy of Abortion Policy API (https://www.abortionpolicyapi.com/)

import requests
import os
import json

APIKEY = os.environ.get("ABORTION_POLICY_API_KEY")
HEADERS = {"token": APIKEY}


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


def get_state_data():
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

    r_gestational = requests.get(gestational_limits_url, headers=HEADERS)
    r_insurance = requests.get(insurance_coverage_url, headers=HEADERS)
    r_minors = requests.get(minors_url, headers=HEADERS)
    r_waiting = requests.get(waiting_periods_url, headers=HEADERS)

    states_gestational = r_gestational.json()
    states_insurance = r_insurance.json()
    states_minors = r_minors.json()
    states_waiting = r_waiting.json()

    return states_gestational, states_insurance, states_minors, states_waiting


def to_json(g, i, m, w):
    """
    Dump state policy data to json file(s)

    Inputs:
        g (list): gestational limit policy by state
        i (list): insurance coverage policy by state
        m (list): minors policy by state
        w (list): waiting periods by state
    """

    # sort states data
    g_sort = sorted(g)
    i_sort = sorted(i)
    m_sort = sorted(m)
    w_sort = sorted(w)

    print("Writing out to json file")

    # one large json file
    with open("data/abortion_policy_api.json", "w") as f:
        json.dump(g_sort, f, indent=1)
        json.dump(i_sort, f, indent=1)
        json.dump(m_sort, f, indent=1)
        json.dump(w_sort, f, indent=1)

    # json file per policy area
    with open("data/abortion_policy_api_gestational.json", "w") as f:
        json.dump(g_sort, f, indent=1)

    with open("data/abortion_policy_api_insurance.json", "w") as f:
        json.dump(i_sort, f, indent=1)

    with open("data/abortion_policy_api_minors.json", "w") as f:
        json.dump(m_sort, f, indent=1)

    with open("data/abortion_policy_api_waiting.json", "w") as f:
        json.dump(w_sort, f, indent=1)


def fix_missing_data(g, i, m, w):
    """
    Fill in missing characteristics for each state

    Inputs:
        g (list): gestational limit policy by state
        i (list): insurance coverage policy by state
        m (list): minors policy by state
        w (list): waiting periods by state
    """

    # TODO
