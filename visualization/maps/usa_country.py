"""
This file contains the functions and functionality needed to render a
hoverable map of the United States of America.

Author(s): Aïcha Camara & Michael Plunkett
"""
from abc import ABC
import plotly.graph_objects as go
import pandas as pd

from visualization.abstract_visualization import Visualization

class USAMap(Visualization, ABC):
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
        #import the files, sort the files, then create the figure 
        #self._import_files()
        #self._sort_files()

        fig = go.Figure(
        data=go.Scattergeo(
        )
        )
        fig.update_geos(
            visible=False,
            resolution=110,
            scope="usa",
            showcountries=True,
            countrycolor="Black",
            showsubunits=True,
            subunitcolor="Black",
        )
        fig.update_layout(height=650, margin={"r": 0, "t": 0, "l": 0, "b": 0})
        config = {"staticPlot": True}
        return fig
