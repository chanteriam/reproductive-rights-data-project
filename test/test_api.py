"""
Tests the api package
"""

import json
from http import HTTPStatus
import responses
from api.abortion_policy_api import (
    get_api_data,
    HEADERS,
    URL_AP_COVERAGE,
    URL_AP_GESTATIONAL_LIMITS,
    URL_AP_MINORS,
    URL_AP_WAITING_PERIODS,
)

# API data stubs
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


# Golden path for main function
@responses.activate
def test_main_golden_path():
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

    test_result = get_api_data()

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


# Cover a potential time out for each call
@responses.activate
def test_get_api_data_gestational_limits_timeout():
    print("test")


@responses.activate
def test_get_api_data_insurance_coverage_timeout():
    print("test")


@responses.activate
def test_get_api_data_minors_timeout():
    print("test")


@responses.activate
def test_get_api_data_waiting_periods_timeout():
    print("test")


@responses.activate
def test_get_api_data_all_timeout():
    print("test")


def test_set_default_types():
    print("test")


def test_fill_in_missing_data():
    print("test")


def test_to_json():
    print("test")
