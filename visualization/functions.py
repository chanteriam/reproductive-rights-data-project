"""
This file contains helper functions for generating data visualizations.
"""

import json

with open("data/clean_ansirh.json") as f:
    NATIONAL_CLINICS = json.load(f)


def get_state_clinic_counts():
    """
    Gets count of abortion clinics in each state.

    Returns:
        (dict): state: clinic count
    """

    count_state_clinics = {}

    for state, zipcodes in NATIONAL_CLINICS.items():
        clinic_count = 0
        for _, clinics in zipcodes.items():
            clinic_count += len(clinics)
        count_state_clinics[state] = clinic_count

    count_state_clinics = dict(sorted(count_state_clinics.items()))
    return count_state_clinics


def get_zipcode_clinic_counts():
    """
    Gets count of abortion clinics in each zipcode.

    Returns:
        (dict): zipcode: clinic count
    """

    count_zipcode_clinics = {}
    for _, zipcodes in NATIONAL_CLINICS.items():
        for zipcode, clinics in zipcodes.items():
            if zipcode == "0.0":
                continue
            count_zipcode_clinics[zipcode] = len(clinics)

    # Sort by count
    count_zipcode_clinics = dict(
        sorted(count_zipcode_clinics.items(), reverse=True, key=lambda x: x[1])
    )

    return count_zipcode_clinics
