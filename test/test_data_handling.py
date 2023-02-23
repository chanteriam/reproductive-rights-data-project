"""
This file contains all testing functions for the repository's data_handling
module.

Author(s): Chanteria Milner
"""

import pandas as pd
import json
from math import isnan
from data_handling.clean_ansirh import (
    clean_ansirh,
    set_default_types,
)
from data_handling.munge_ansirh import (
    split_by_state,
    translate_code_to_state,
    split_by_zip,
    make_row_dicts,
)


DATA = {
    "facility ID": [1, 2],
    "name": ["Clinic 1", "Clinic 2"],
    "city": ["Chicago", "Dallas"],
    "state": ["IL", "TX"],
    "zip code": [60637.0, 72001.0],
    "open in 2021": [float("nan"), "No"],
    "provided abortions in 2021": [" YES", "no"],
}

ROWS = [
    {
        "facility ID": 1,
        "name": "Clinic 1",
        "city": "Chicago",
        "state": "IL",
        "zip code": 60637.0,
        "open in 2021": float("nan"),
        "provided abortions in 2021": " YES",
    },
    {
        "facility ID": 2,
        "name": "Clinic 2",
        "city": "Dallas",
        "state": "TX",
        "zip code": 72001.0,
        "open in 2021": "No",
        "provided abortions in 2021": "no",
    },
]

CORRECT_DEFAULT_TYPES = {
    "facility ID": 0,
    "name": None,
    "city": None,
    "state": None,
    "zip code": 0.0,
    "open in 2021": None,
    "provided abortions in 2021": None,
}

DF = pd.DataFrame(DATA)

STATES = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "District of Columbia",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]

STATE_ABRS = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "DC",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]


def test_make_row_dicts():
    rows = make_row_dicts(DF)
    for i, row in enumerate(ROWS):
        for k, v in row.items():
            if not isinstance(v, str) and isnan(v):
                assert isnan(rows[i][k])
            else:
                assert rows[i][k] == v


def test_set_default_types():
    assert set_default_types(ROWS) == CORRECT_DEFAULT_TYPES


def test_clean_ansirh():
    clean_rows = [
        {
            "facility ID": "1",
            "name": "clinic 1",
            "city": "chicago",
            "state": "il",
            "zip code": "60637",
            "open in 2021": None,
            "provided abortions in 2021": True,
        },
        {
            "facility ID": "2",
            "name": "clinic 2",
            "city": "dallas",
            "state": "tx",
            "zip code": "72001",
            "open in 2021": False,
            "provided abortions in 2021": False,
        },
    ]

    assert clean_ansirh(ROWS) == clean_rows


def test_translate_code_to_state():
    for i, abr in enumerate(STATE_ABRS):
        assert translate_code_to_state(abr) == STATES[i]


# TODO - Write this test
def test_split_by_state():
    print("test")


# TODO - Write this test
def test_split_by_zip():
    print("test")


# TODO - Write this test
def test_to_json():
    print("test")
