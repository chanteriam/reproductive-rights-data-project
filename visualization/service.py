"""
This file works as the central point for running the visualization package.
"""
from visualization.app import DASH_INSTANCE, build_dash
from util.constants import FILE_NAME_ABORTION_POLICY_API_GESTATION, \
FILE_NAME_ABORTION_POLICY_API_INSURANCE, FILE_NAME_ABORTION_POLICY_API_MINORS, \
FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD, FILE_NAME_ANSIRH_CLEAN_DATA

def main():
    """
    Author(s): Michael Plunkett
    """
    # TODO: Build charts here

    # Use the actual file name to instantiate the filenames, use the constants
    # in utils

    country_chart = None
    country_map = None
    state_map = None

    build_dash(country_chart, country_map, state_map)

    DASH_INSTANCE.run_server(host="localhost", port=8005)
