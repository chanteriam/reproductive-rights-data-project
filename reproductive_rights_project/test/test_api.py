"""
This file contains all testing functions for the api package.
"""

import json
import os
from http import HTTPStatus

import responses

from reproductive_rights_project.api.abortion_policy_api import (
    HEADERS,
    URL_AP_COVERAGE,
    URL_AP_GESTATIONAL_LIMITS,
    URL_AP_MINORS,
    URL_AP_WAITING_PERIODS,
    add_missing_states,
    fill_in_missing_data,
    get_data,
    set_default_types,
)
from reproductive_rights_project.api.github.open_data_se import (
    get_state_zip_code_geo_json,
)
from reproductive_rights_project.util.constants import BASE_DATA_DIR
from reproductive_rights_project.util.functions import to_json

# API data stubs
CORRECT_KEY_DEFAULTS = {
    "exception_rape_or_incest": False,
    "exception_health": None,
    "banned_after_weeks_since_LMP": 0,
    "exception_life": False,
    "Last Updated": None,
    "exception_fetal": False,
}

gestational_data = json.dumps(
    {
        "A state": {
            "exception_rape_or_incest": True,
            "exception_health": "Physical",
            "banned_after_weeks_since_LMP": 0,
            "exception_life": True,
            "Last Updated": "2022-12-29T21:34:59.000Z",
            "exception_fetal": None,
        }
    }
)

insurance_data = json.dumps(
    {
        "A state": {
            "medicaid_exception_rape_or_incest": True,
            "medicaid_exception_life": True,
            "exchange_coverage_no_restrictions": True,
            "private_coverage_no_restrictions": True,
            "medicaid_exception_fetal": "Serious fetal anomaly",
            "medicaid_coverage_provider_patient_decision": False,
            "medicaid_exception_health": None,
            "exchange_exception_rape_or_incest": False,
            "exchange_exception_life": False,
            "private_exception_health": None,
            "exchange_exception_health": None,
            "private_exception_life": False,
            "private_exception_rape_or_incest": False,
            "requires_coverage": False,
            "Last Updated": None,
            "exchange_forbids_coverage": False,
            "private_exception_fetal": None,
            "exchange_exception_fetal": None,
        },
    }
)

minors_data = json.dumps(
    {
        "A state": {
            "parental_consent_required": True,
            "judicial_bypass_available": True,
            "below_age": 18,
            "parents_required": 1,
            "allows_minor_to_consent_to_abortion": False,
            "parental_notification_required": False,
            "Last Updated": None,
        }
    }
)

waiting_data = json.dumps(
    {
        "A state": {
            "waiting_period_hours": 24,
            "counseling_visits": 2,
            "counseling_waived_condition": None,
            "Last Updated": None,
            "waiting_period_notes": None,
        }
    }
)


@responses.activate
def test_get_api_data():
    """
    Tests functionality of abortion_policy_api.get_data().
    """
    responses.add(
        responses.GET,
        URL_AP_GESTATIONAL_LIMITS,
        headers=HEADERS,
        json=gestational_data,
        status=HTTPStatus.OK,
    )

    responses.add(
        responses.GET,
        URL_AP_COVERAGE,
        headers=HEADERS,
        json=insurance_data,
        status=HTTPStatus.OK,
    )

    responses.add(
        responses.GET,
        URL_AP_MINORS,
        headers=HEADERS,
        json=minors_data,
        status=HTTPStatus.OK,
    )

    responses.add(
        responses.GET,
        URL_AP_WAITING_PERIODS,
        headers=HEADERS,
        json=waiting_data,
        status=HTTPStatus.OK,
    )

    test_result = get_data()

    # Verify the right amount of objects are coming back
    assert len(test_result) == 4
    assert test_result[0] == gestational_data
    assert test_result[1] == insurance_data
    assert test_result[2] == minors_data
    assert test_result[3] == waiting_data

    # Assert the URLs are being called the correct amount of times
    assert responses.assert_call_count(URL_AP_GESTATIONAL_LIMITS, 1) is True
    assert responses.assert_call_count(URL_AP_COVERAGE, 1) is True
    assert responses.assert_call_count(URL_AP_MINORS, 1) is True
    assert responses.assert_call_count(URL_AP_WAITING_PERIODS, 1) is True


@responses.activate
def test_get_state_zip_code_geo_json_first_call():
    """
    Tests functionality of open_data_se.get_state_zip_code_geo_json()'s first
    call.
    """
    test_data = json.dumps({"data": "here it is"})
    file_name = "nas_not_a_state_zip_codes_geo.min.json"
    test_url = (
        f"https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON"
        f"/master/{file_name}"
    )

    responses.add(
        responses.GET,
        test_url,
        headers=HEADERS,
        json=test_data,
        status=HTTPStatus.OK,
    )

    test_result = get_state_zip_code_geo_json("NaS", "Not a State")

    assert test_result == test_data
    assert responses.assert_call_count(test_url, 1) is True
    assert os.path.exists(BASE_DATA_DIR + file_name)

    os.remove(BASE_DATA_DIR + file_name)

    assert not os.path.exists(BASE_DATA_DIR + file_name)


@responses.activate
def test_get_state_zip_code_geo_json_not_first_call():
    """
    Tests functionality of open_data_se.get_state_zip_code_geo_json() beyond
    its first call.
    """
    test_data = json.dumps({"data": "here it be"})
    file_name = "naz_not_a_zebra_zip_codes_geo.min.json"
    test_url = (
        f"https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON"
        f"/master/{file_name}"
    )

    responses.add(
        responses.GET,
        test_url,
        headers=HEADERS,
        json=test_data,
        status=HTTPStatus.OK,
    )

    to_json([test_data], [BASE_DATA_DIR + file_name])

    test_result = get_state_zip_code_geo_json("NaZ", "Not a Zebra")

    assert test_result == test_data
    assert responses.assert_call_count(test_url, 0) is True
    assert os.path.exists(BASE_DATA_DIR + file_name)

    os.remove(BASE_DATA_DIR + file_name)

    assert not os.path.exists(BASE_DATA_DIR + file_name)


def test_set_default_types():
    """
    Tests functionality of abortion_policy_api.set_default_types().
    """
    policies = {
        "State1": {
            "exception_rape_or_incest": True,
            "exception_health": "Physical",
            "exception_life": True,
            "Last Updated": "2022-08-29T21:34:59.000Z",
        },
        "State2": {
            "exception_health": "Major Bodily Function",
            "banned_after_weeks_since_LMP": 24,
            "exception_life": True,
            "exception_fetal": True,
        },
    }

    key_defaults = set_default_types(policies)

    # Verify the right amount of objects are coming back
    assert len(key_defaults.keys()) == len(CORRECT_KEY_DEFAULTS.keys())

    # Assert correct key-value pairs
    for key, value in CORRECT_KEY_DEFAULTS.items():
        assert key_defaults[key] == value


def test_fill_in_missing_data():
    """
    Tests functionality of abortion_policy_api.fill_in_missing_data().
    """
    policies = {
        "A state": {
            "exception_rape_or_incest": True,
            "exception_health": "Physical",
            "exception_life": True,
            "Last Updated": "2022-12-29T21:34:59.000Z",
        },
    }

    expected = json.loads(gestational_data)

    fill_in_missing_data(policies, CORRECT_KEY_DEFAULTS)

    # Verify the right amount of objects are coming back
    assert len(policies["A state"]) == len(CORRECT_KEY_DEFAULTS)

    # Assert correct keys
    for key in expected["A state"]:
        assert key in policies["A state"]


def test_add_missing_states():
    """
    Tests functionality of abortion_policy_api.add_missing_states().
    """
    states = ["A state", "Another state"]

    policies = json.loads(gestational_data)

    expected = {
        "Another state": {
            "exception_rape_or_incest": False,
            "exception_health": None,
            "banned_after_weeks_since_LMP": 0,
            "exception_life": False,
            "Last Updated": None,
            "exception_fetal": False,
        }
    }

    add_missing_states(policies, CORRECT_KEY_DEFAULTS, states)

    # Verify correct number of states in dictionary
    assert len(policies) == len(states)

    # Verify addition of third state
    assert policies["Another state"]

    # Verify key-values of added state
    for key, value in expected["Another state"].items():
        assert policies["Another state"][key] == value
