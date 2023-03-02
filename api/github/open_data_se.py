"""
This file interfaces with the OpenDataSE GitHub repository.
"""

import requests
from util.constants import REQUEST_TIMEOUT


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

    state_zip_geo_info = requests.get(
        f"https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON"
        f"/master/{state_abbrev}_{state_name}_zip_codes_geo.min.json",
        timeout=REQUEST_TIMEOUT,
    )

    return state_zip_geo_info.json()
