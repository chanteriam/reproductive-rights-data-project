"""
This file works as the central point for running the visualization package.
"""
from visualization.app import DASH_INSTANCE, build_dash
from visualization.maps.usa_country import USAMap as USAMap
from visualization.maps.usa_state import USAState as USAState
from visualization.charts.state_summary import StateSummary as StateSummary
from util.constants import (
    FILE_NAME_ABORTION_POLICY_API_GESTATION,
    FILE_NAME_ABORTION_POLICY_API_INSURANCE,
    FILE_NAME_ABORTION_POLICY_API_MINORS,
    FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
    FILE_NAME_ANSIRH_CLEAN_DATA,
    FILE_NAME_STATE_ABBREVIATIONS
)


def main():
    """
    Author(s): Michael Plunkett
    """
    # TODO: Build charts here

    # Use the actual file name to instantiate the filenames, use the constants
    # in utils

    country_chart = USAState(FILE_NAME_ABORTION_POLICY_API_GESTATION, 
                            FILE_NAME_ABORTION_POLICY_API_INSURANCE, 
                            FILE_NAME_ABORTION_POLICY_API_MINORS, 
                            FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD, 
                            FILE_NAME_ANSIRH_CLEAN_DATA)
    
    country_map = USAMap(FILE_NAME_ABORTION_POLICY_API_GESTATION, 
                         FILE_NAME_ANSIRH_CLEAN_DATA, 
                         FILE_NAME_STATE_ABBREVIATIONS)
    
    state_map = StateSummary(FILE_NAME_ABORTION_POLICY_API_GESTATION,
                             FILE_NAME_ABORTION_POLICY_API_INSURANCE,
                             FILE_NAME_ANSIRH_CLEAN_DATA,
                             FILE_NAME_ABORTION_POLICY_API_MINORS,
                             FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD

    )

    build_dash(country_chart, country_map, state_map)

    DASH_INSTANCE.run_server(host="localhost", port=8005)
