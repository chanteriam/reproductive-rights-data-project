"""
This file works as the central point for running the visualization package.
"""
from visualization.app import DASH_INSTANCE, build_dash


def main():
    """
    Author(s): Michael Plunkett
    """
    # TODO: Build charts here

    country_chart = None
    country_map = None
    state_map = None

    build_dash(country_chart, country_map, state_map)

    DASH_INSTANCE.run_server(host="localhost", port=8005)
