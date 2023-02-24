"""
This file contains all testing functions for the repository's data_handling
module.

Author(s): Chanteria Milner
"""

import pandas as pd
import os
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
    to_json,
)

# Data for testing
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

STATES = []
STATE_ABRS = []
states_fname = "data/state_abbreviations.csv"
with open(states_fname, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        state, abbrev, code = line.split(",")
        STATES.append(state.strip('"'))
        STATE_ABRS.append(code.strip('"'))

STATES.pop(0)
STATE_ABRS.pop(0)


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


def test_split_by_state():
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
        {
            "facility ID": "3",
            "name": "clinic 3",
            "city": "houston",
            "state": "tx",
            "zip code": "77001",
            "open in 2021": True,
            "provided abortions in 2021": False,
        },
    ]

    split_rows = {
        "Illinois": [
            {
                "facility ID": "1",
                "name": "clinic 1",
                "city": "chicago",
                "state": "il",
                "zip code": "60637",
                "open in 2021": None,
                "provided abortions in 2021": True,
            }
        ],
        "Texas": [
            {
                "facility ID": "2",
                "name": "clinic 2",
                "city": "dallas",
                "state": "tx",
                "zip code": "72001",
                "open in 2021": False,
                "provided abortions in 2021": False,
            },
            {
                "facility ID": "3",
                "name": "clinic 3",
                "city": "houston",
                "state": "tx",
                "zip code": "77001",
                "open in 2021": True,
                "provided abortions in 2021": False,
            },
        ],
    }

    rows = split_by_state(clean_rows)
    assert len(rows["Texas"]) == 2
    assert rows == split_rows


def test_split_by_zip():
    split_rows_state = {
        "Illinois": [
            {
                "facility ID": "1",
                "name": "clinic 1",
                "city": "chicago",
                "state": "il",
                "zip code": "60637",
                "open in 2021": None,
                "provided abortions in 2021": True,
            }
        ],
        "Texas": [
            {
                "facility ID": "2",
                "name": "clinic 2",
                "city": "dallas",
                "state": "tx",
                "zip code": "72001",
                "open in 2021": False,
                "provided abortions in 2021": False,
            },
            {
                "facility ID": "3",
                "name": "clinic 3",
                "city": "dallas",
                "state": "tx",
                "zip code": "72001",
                "open in 2021": True,
                "provided abortions in 2021": False,
            },
        ],
    }

    split_rows_zip = {
        "Illinois": {
            "60637": [
                {
                    "facility ID": "1",
                    "name": "clinic 1",
                    "city": "chicago",
                    "state": "il",
                    "zip code": "60637",
                    "open in 2021": None,
                    "provided abortions in 2021": True,
                }
            ]
        },
        "Texas": {
            "72001": [
                {
                    "facility ID": "2",
                    "name": "clinic 2",
                    "city": "dallas",
                    "state": "tx",
                    "zip code": "72001",
                    "open in 2021": False,
                    "provided abortions in 2021": False,
                },
                {
                    "facility ID": "3",
                    "name": "clinic 3",
                    "city": "dallas",
                    "state": "tx",
                    "zip code": "72001",
                    "open in 2021": True,
                    "provided abortions in 2021": False,
                },
            ],
        },
    }

    rows = split_by_zip(split_rows_state)
    assert len(rows["Texas"]["72001"]) == 2
    assert split_rows_zip == rows


def test_to_json():
    file_name = "data/test_file1.json"

    to_json(ROWS, file_name)

    # assert existence of file
    assert os.path.exists(file_name)
    os.remove(file_name)
