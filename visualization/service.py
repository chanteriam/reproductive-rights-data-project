"""
This file works as the central point for running the visualization package.
"""
from visualization.app import DASH_INSTANCE


def main():
    """
    Author(s): Michael Plunkett
    """
    DASH_INSTANCE.run_server(host="localhost", port=8005)
