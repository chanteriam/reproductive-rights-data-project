"""
This file works as the central point for running the data_handling package.
"""
import os

from reproductive_rights_data_project.data_handling.ansirh.process import (
    clean_and_save,
)
from reproductive_rights_data_project.util.constants import (
    FILE_NAME_ANSIRH_BASE_DATA,
)


def main():
    """
    Runs all processes related to data handling.

    Returns (None):
        Writes JSON file with cleaned and formatted application data.
    """

    # Require the presence of the original ANSIRH file to run the data-parsing
    # package.
    assert os.path.exists(FILE_NAME_ANSIRH_BASE_DATA)

    # Clean and save ANSIRH data.
    clean_and_save()
