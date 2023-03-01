"""
This file contains the functions and functionality needed to render a
map of the United States of America.
"""
from abc import ABC
import plotly.express as px
import pandas as pd

from visualization.abstract_visualization import Visualization
from visualization.functions import get_state_clinic_counts


class USAMap(Visualization, ABC):
    """
    This class is an extension of the Visualization abstract class and creates
    a map of the USA in plotly.

    Author(s): Aïcha Camara, Michael Plunkett
    """

    def __init__(self, files):
        # File names are passed from outside the class and stored in the
        # below variable
        self._files = files
        pass

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        # Put this functionality inside here, plz
        return get_state_clinic_counts()

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization
        """
        abbreviations = pd.read_csv("data/state_abbreviations.csv")
        extract_abbrev = abbreviations["code"]

        state_dict = self._import_files()
        state_df = pd.DataFrame(state_dict.items(), columns=["state", "count"])
        state_df = state_df.join(extract_abbrev)

        return state_df

    def construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USA country visual.
        """
        # Call all of your _import, _sort, etc. functions here and save the
        # data to internal variables

    def create(self):
        """
        Creates the map of a United States state using the data from the
        construct function and returns the plotly map of a state.
        """
        # Take the information from construct_data function and use it to build
        # your map here
        state_df = self._sort_files()

        fig = px.choropleth(
            state_df,
            locations="code",
            hover_name="state",
            hover_data=["count"],
            locationmode="USA-states",
            labels={"count": "Clinic Count"},
            scope="usa",
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
        return fig
