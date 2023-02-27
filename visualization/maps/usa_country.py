"""
This file contains the functions and functionality needed to render a
hoverable map of the United States of America.
"""
from abc import ABC
import plotly.graph_objects as go

from visualization.abstract_visualization import Visualization

class USAMap(Visualization, ABC):
    def __init__(self, files):
        pass
    def create_figure():
        """
        Creates the map of the United States
        """
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
