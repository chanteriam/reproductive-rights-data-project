"""
This file works as the central point for running the visualization package.
"""
from reproductive_rights_data_project.visualization.app import (
    DASH_INSTANCE,
    build_dash,
)
from reproductive_rights_data_project.visualization.maps.usa_country import (
    USAMap,
)
from reproductive_rights_data_project.visualization.charts.state_summary import (
    StateSummary,
)
from reproductive_rights_data_project.visualization.charts.zip_code import (
    ZipChart,
)
from reproductive_rights_data_project.visualization.maps.city import (
    CityBar,
)
from reproductive_rights_data_project.util.constants import (
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

    zip_chart = ZipChart(FILE_NAME_ANSIRH_CLEAN_DATA)

    city_bar = CityBar(FILE_NAME_ANSIRH_CLEAN_DATA)

    build_dash(country_chart, country_map, zip_chart, city_bar)

    DASH_INSTANCE.run_server(host="localhost", port=8005)
