"""
This file works as the central point for running the api package.
"""

from reproductive_rights_project.api.abortion_policy_api import (
    ABORTION_POLICY_API_KEY,
    get_and_save_abortion_policy_api_data,
)


def main():
    """
    Runs all processes related to external APIs.

    Returns (None):
        Writes JSON file with cleaned and formatted application data.
    """

    # Require the Abortion Policy API key for the api package to run.
    assert ABORTION_POLICY_API_KEY != ""

    get_and_save_abortion_policy_api_data()
