"""
This file contains all testing functions for the util package.
"""

import json
import os

from reproductive_rights_data_project.util.constants import STANDARD_ENCODING
from reproductive_rights_data_project.util.functions import to_json


def test_to_json():
    """
    Tests functionality of util.to_json().
    """
    rows = [
        {
            "facility ID": 3,
            "name": "Clinic 3",
            "city": "Chicago",
            "state": "IL",
            "zip code": 60637.0,
            "open in 2021": float("nan"),
            "provided abortions in 2021": " YES",
        },
        {
            "facility ID": 4,
            "name": "Clinic 4",
            "city": "Dallas",
            "state": "TX",
            "zip code": 72001.0,
            "open in 2021": "No",
            "provided abortions in 2021": "no",
        },
    ]

    file_name = "reproductive_rights_data_project/data/test_file1.json"

    to_json([rows], [file_name])

    # assert existence of file
    assert os.path.exists(file_name)

    with open(file_name, "r", encoding=STANDARD_ENCODING) as f:
        data = json.load(f)
        assert len(data) == len(rows)
        for i, d in enumerate(data):
            assert d["facility ID"] == rows[i]["facility ID"]

    os.remove(file_name)
