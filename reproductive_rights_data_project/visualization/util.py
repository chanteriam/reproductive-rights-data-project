"""
Utility functions for the visualization package.
"""


def sort_by_count(clinic_counts):
    """
    Sorts a dictionary of clinic counts in descending order.

    Inputs:
        clinic_counts (dict): count of clinics by either state, zipcode, or city

    Returns (dict):
        Returns a sorted dictionary.
    """

    clinic_counts = dict(
        sorted(clinic_counts.items(), reverse=True, key=lambda x: x[1])
    )
    return clinic_counts
