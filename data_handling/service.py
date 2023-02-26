"""
This file works as the central point for running the data_handling package.
"""

from data_handling.ansirh.process import clean_and_save


def main():
    """
    Runs all processes related to data handling.

    Returns (None):
        Writes JSON file with cleaned and formatted application data.
    """

    # Clean and save ANSIRH data
    clean_and_save()
