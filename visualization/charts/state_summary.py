"""
This file contains the functions and functionality needed to display a State
summary of abortion-related data.
"""
from abc import ABC

from visualization.abstract_visualization import Visualization

class StateSummary(Visualization, ABC):
    def __init__(self, files):
        pass

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        pass

    def _sort_files(self):
        pass
        
    def create(self):
        """
        Creates the map of the United States
        """
        pass
