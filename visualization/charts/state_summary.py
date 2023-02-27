"""
This file contains the functions and functionality needed to display a State
summary of abortion-related data.

Author(s): Aïcha Camara & Michael Plunkett
"""
from abc import ABC
import plotly.graph_objects as go
import pandas as pd

from visualization.abstract_visualization import Visualization

class StateSummary(Visualization, ABC):
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
        Creates the state summary chart
        """
        pass
        # figure = go.Figure()
