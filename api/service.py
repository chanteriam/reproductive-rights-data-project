"""
This file works as the central point for running the api package.
"""

from api.abortion_policy_api import get_and_save_abortion_policy_api_data


def main():
    """
    Runs all processes related to external APIs.

    Author(s): Michael Plunkett

    Returns (None):
        Writes JSON file with cleaned and formatted application data.
    """

    get_and_save_abortion_policy_api_data()
