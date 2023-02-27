"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.
"""
from abc import ABC

from visualization.abstract_visualization import Visualization

class USAState(Visualization, ABC):
    def __init__(self, files):
        pass

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        pass

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization
        """
        pass
        
    def create(self):
        """
        Creates the map of the United States
        """
        pass