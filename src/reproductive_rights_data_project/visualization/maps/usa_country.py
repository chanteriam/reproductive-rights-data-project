"""
This file contains the functions and functionality needed to render a
map of the United States of America.
"""
import plotly.express as px
import pandas as pd
import json

from src.reproductive_rights_data_project.visualization.abstract_visualization import (
    Visualization,
)
from src.reproductive_rights_data_project.util.constants import (
    STANDARD_ENCODING,
)


class USAMap(Visualization):
    """
    This class is an extension of the Visualization abstract class and creates
    a map of the USA in plotly.

    Author(s): Aïcha Camara, Michael Plunkett
    """

    def __init__(
        self,
        gestational_info_file_name,
        locations_file_name,
        state_abbrevs_file_name,
    ):
        """
        Author(s): Michael Plunkett
        """
        self._gestational_info_file_name = gestational_info_file_name
        self._gestational_info = None
        self._locations_file_name = locations_file_name
        self._locations = None
        self._state_abbrevs_file_name = state_abbrevs_file_name
        self._state_abbrevs = None

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.

        Author(s): Aïcha Camara
        """

        with open(
            self._gestational_info_file_name, encoding=STANDARD_ENCODING
        ) as gestational, open(
            self._locations_file_name, encoding=STANDARD_ENCODING
        ) as locations, open(
            self._state_abbrevs_file_name, encoding=STANDARD_ENCODING
        ) as abbreviations:
            self._gestational_info = json.load(gestational)
            self._locations = json.load(locations)
            self._state_abbrevs = pd.read_csv(abbreviations)

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization

        Author(s): Aïcha Camara, Chanteria Milner
        """

        # extract the abbreviations from the abbreviations column
        extracted_abbrev = self._state_abbrevs["code"]

        # sort gestational data and extract the necessary columns
        gest_df = pd.DataFrame.from_dict(
            self._gestational_info, orient="index"
        ).sort_index()
        gest_df = gest_df.reset_index().rename(columns={"index": "state"})
        # extracted_gest = gest_df[['state','exception_life', 'banned_after_weeks_since_LMP']]

        # sorts locations data to get counts by state
        count_state_clinics = {}

        for state, zipcodes in self._locations.items():
            clinic_count = 0
            for _, clinics in zipcodes.items():
                clinic_count += len(clinics)
            count_state_clinics[state] = clinic_count

        count_state_clinics = dict(sorted(count_state_clinics.items()))
        state_df = pd.DataFrame(
            count_state_clinics.items(), columns=["state", "count"]
        )
        state_df = state_df.join(extracted_abbrev)

        final_df = pd.merge(
            state_df,
            gest_df[
                ["state", "exception_life", "banned_after_weeks_since_LMP"]
            ],
            on="state",
        )

        return final_df

    def construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USA country visual.

        Author(s): Aïcha Camara
        """

        self._import_files()
        state_df = self._sort_files()

        return state_df

    def create_visual(self):
        """
        Creates the map of a United States state using the data from the
        construct function and returns the plotly map of a state.

        Author(s): Aïcha Camara
        """

        state_df = self.construct_data()

        fig = px.choropleth(
            state_df,
            locations="code",
            hover_name="state",
            hover_data=[
                "count",
                "exception_life",
                "banned_after_weeks_since_LMP",
            ],
            locationmode="USA-states",
            labels={
                "count": "Clinic Count: ",
                "exception_life": "Exception for life at risk? ",
                "banned_after_weeks_since_LMP": "Abortion banned after how many weeks? ",
            },
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
