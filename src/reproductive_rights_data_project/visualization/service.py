"""
This file works as the central point for running the visualization package.

Author(s): Michael Plunkett and Aïcha Camara
"""
from src.reproductive_rights_data_project.visualization.app import (
    DASH_INSTANCE,
    build_dash,
)
from src.reproductive_rights_data_project.visualization.maps.usa_country import (
    USAMap as USAMap,
)
from src.reproductive_rights_data_project.visualization.maps.usa_state import (
    USAState as USAState,
)
from src.reproductive_rights_data_project.visualization.charts.state_summary import (
    StateSummary as StateSummary,
)
from src.reproductive_rights_data_project.util.constants import (
    FILE_NAME_ABORTION_POLICY_API_GESTATION,
    FILE_NAME_ABORTION_POLICY_API_INSURANCE,
    FILE_NAME_ABORTION_POLICY_API_MINORS,
    FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
    FILE_NAME_ANSIRH_CLEAN_DATA,
    FILE_NAME_STATE_ABBREVIATIONS,
)


def main():
    """
    Author(s): Michael Plunkett and Aïcha Camara
    """

    country_chart = StateSummary(
        FILE_NAME_ABORTION_POLICY_API_GESTATION,
        FILE_NAME_ABORTION_POLICY_API_INSURANCE,
        FILE_NAME_ANSIRH_CLEAN_DATA,
        FILE_NAME_ABORTION_POLICY_API_MINORS,
        FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
    )

    country_map = USAMap(
        FILE_NAME_ABORTION_POLICY_API_GESTATION,
        FILE_NAME_ANSIRH_CLEAN_DATA,
        FILE_NAME_STATE_ABBREVIATIONS,
    )

    state_map = USAState(
        FILE_NAME_ABORTION_POLICY_API_GESTATION,
        FILE_NAME_ABORTION_POLICY_API_INSURANCE,
        FILE_NAME_ABORTION_POLICY_API_MINORS,
        FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD,
        FILE_NAME_ANSIRH_CLEAN_DATA,
    )

    build_dash(country_chart, country_map, state_map)

    DASH_INSTANCE.run_server(host="localhost", port=8005)