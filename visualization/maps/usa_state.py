"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.

Author(s): Aïcha Camara & Michael Plunkett
"""
from abc import ABC
import pandas as pd

from visualization.abstract_visualization import Visualization

class USAState(Visualization, ABC):
    def __init__(self, files):
        self.files = files

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