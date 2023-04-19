"""
This file contains all testing functions for the data_handling package.
"""

from math import isnan

import pandas as pd

from reproductive_rights_project.data_handling.ansirh.clean import (
    clean,
    set_default_types,
)
from reproductive_rights_project.data_handling.ansirh.process import (
    make_row_dicts,
    split_by_state,
    split_by_zip,
    translate_code_to_state,
)
from reproductive_rights_project.util.constants import (
    FILE_NAME_STATE_ABBREVIATIONS,
    STANDARD_ENCODING,
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
STATE_ABRVS = []
with open(FILE_NAME_STATE_ABBREVIATIONS, "r", encoding=STANDARD_ENCODING) as f:
    for line in f:
        line = line.strip()
        state, abbrev, code = line.split(",")
        STATES.append(state.strip('"'))
        STATE_ABRVS.append(code.strip('"'))

# Getting rid of headers
STATES.pop(0)
STATE_ABRVS.pop(0)


def test_make_row_dicts():
    """
    Tests functionality of data_handling.ansirh.process.make_row_dicts().
    """
    rows = make_row_dicts(DF)
    for i, row in enumerate(ROWS):
        for k, v in row.items():
            if not isinstance(v, str) and isnan(v):
                assert isnan(rows[i][k])
            else:
                assert rows[i][k] == v


def test_set_default_types():
    """
    Tests functionality of data_handling.ansirh.clean.set_default_types().

    """
    assert set_default_types(ROWS) == CORRECT_DEFAULT_TYPES


def test_clean_ansirh():
    """
    Tests functionality of data_handling.ansirh.clean.clean().
    """
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

    assert clean(ROWS) == clean_rows


def test_translate_code_to_state():
    """
    Tests functionality of util.functions.translate_code_to_state().
    """
    for i, abr in enumerate(STATE_ABRVS):
        assert translate_code_to_state(abr) == STATES[i]


def test_split_by_state():
    """
    Tests functionality of data_handling.ansirh.process.split_by_state().
    """
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
    """
    Tests functionality of data_handling.ansirh.process.split_by_zip().
    """
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
