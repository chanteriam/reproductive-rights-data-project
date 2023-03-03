"""
This file contains helper functions for generating data visualizations.
"""

import json
from reproductive_rights_data_project.util.constants import (
    FILE_NAME_ANSIRH_CLEAN_DATA,
    STANDARD_ENCODING,
)

# Maybe not good for testability
with open(FILE_NAME_ANSIRH_CLEAN_DATA, encoding=STANDARD_ENCODING) as f:
    NATIONAL_CLINICS = json.load(f)


def get_state_clinic_counts():
    """
    Gets count of abortion clinics in each state.

    Author(s): Chanteria Milner

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


def get_city_clinic_counts():
    """
    Gets count of abortion clinics in each city.
    Author(s): Chanteria Milner

    Returns:
        (dict): zipcode: clinic count
    """

    count_city_clinics = {}
    for state, zipcodes in NATIONAL_CLINICS.items():
        for zipcode, clinics in zipcodes.items():
            if zipcode == "0.0":  # missing value
                continue
            for clinic in clinics:
                if clinic["city"] == 0.0:  # missing value
                    continue
                city_state = ", ".join([clinic["city"].title(), state])
                count_city_clinics[city_state] = (
                        count_city_clinics.get(city_state, 0) + 1
                )

    # sort by number of clinics
    count_city_clinics = sort_by_count(count_city_clinics)
    return count_city_clinics


def get_zipcode_clinic_counts():
    """
    Gets count of abortion clinics in each zipcode.
    Author(s): Chanteria Milner

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
    count_zipcode_clinics = sort_by_count(count_zipcode_clinics)
    return count_zipcode_clinics


def sort_by_count(clinic_counts):
    """
    Sorts a dictionary of clinic counts in descending order.
    Author(s): Chanteria Milner

    Inputs:
        clinic_counts (dict): count of clinics by either state, zipcode, or city

    Returns:
        (dict): sorted dictionary
    """

    clinic_counts = dict(
        sorted(clinic_counts.items(), reverse=True, key=lambda x: x[1])
    )
    return clinic_counts


def read_state():
    """
    Creates an alphabetical list of states for
    the state downdown navigation bar

    Author(s): Aïcha Camara

    Returns:
        (list) list of states in alphabetical order
    """

    with open("./data/states.txt", encoding=STANDARD_ENCODING) as state:
        state_lst = [line.strip() for line in state.readlines()]
    return state_lst
