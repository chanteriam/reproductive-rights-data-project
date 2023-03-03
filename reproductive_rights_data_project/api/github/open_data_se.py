"""
This file interfaces with the OpenDataSE GitHub repository.
"""
import json
import os.path

import requests
from reproductive_rights_data_project.util.constants import (
    BASE_DATA_DIR,
    REQUEST_TIMEOUT,
    STANDARD_ENCODING,
)
from reproductive_rights_data_project.util.functions import to_json


def get_state_zip_code_geo_json(state_abbrev, state_name):
    """
    This function calls the OpenDataSE State-zip-code-GeoJSON GitHub repository
    and returns a given state's zip code geo json file.

    Author(s): Michael Plunkett

    Inputs:
        state_abbrev (string): the abbreviation for the state you are seeking
        state_name (string): the name of the state you are seeking

    Returns (dict):
        A state's zip code boundary information in JSON format.
    """

    state_abbrev = state_abbrev.lower()
    state_name = state_name.lower().replace(" ", "_")

    file_name = f"{state_abbrev}_{state_name}_zip_codes_geo.min.json"
    file_name_and_path = BASE_DATA_DIR + file_name

    # If we have already accessed this data, then we pull from the file
    # and don't hit the API.
    if os.path.exists(file_name_and_path):
        with open(file_name_and_path, "r", encoding=STANDARD_ENCODING) as f:
            state_zip_geo_info = json.load(f)

        return state_zip_geo_info

    state_zip_geo_info = requests.get(
        f"https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON"
        f"/master/{file_name}",
        timeout=REQUEST_TIMEOUT,
    )

    state_zip_geo_info_json = state_zip_geo_info.json()

    to_json([state_zip_geo_info_json], [file_name_and_path])

    return state_zip_geo_info_json
