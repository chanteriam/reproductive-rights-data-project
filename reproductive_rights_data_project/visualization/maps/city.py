"""
This file contains the functions and functionality needed to display a
visualization of the top 25 cities with abortion clinics
"""
import json
import plotly.express as px
import pandas as pd

from reproductive_rights_data_project.visualization.abstract_visualization import (
    Visualization,
)
from reproductive_rights_data_project.util.constants import (
    STANDARD_ENCODING,
)


class CityBar(Visualization):
    """
    This class represents a table with information on each state.

    Author(s): Aïcha Camara
    """

    def __init__(
        self,
        locations_file_name,
    ):
        """
        Author(s): Aïcha Camara
        """
        self._locations_file_name = locations_file_name
        self._locations = None

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.

        Author(s): Aïcha Camara
        """
        with open(
            self._locations_file_name, encoding=STANDARD_ENCODING
        ) as locations:
            self._locations = json.load(locations)

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization

        Author(s): Chanteria Milner, Aicha Camara
        """

        # sorts locations data to get counts by state
        count_city_clinics = self._count_by_city()

        # count_city_clinics = dict(sorted(count_city_clinics.items()))
        count_city_clinics = dict(
            sorted(count_city_clinics.items(), key=lambda x: x[1])
        )
        city_df = pd.DataFrame(
            count_city_clinics.items(), columns=["City", "Clinic Count"]
        )

        return city_df

    def _count_by_city(self):
        """
        This method provides a count of abortion clinics by city.

        Author(s): Chanteria Milner, Aicha Camara

        Returns:
            (dict) city, state: clinic count
        """

        count_city_clinics = {}
        for state, zipcodes in self._locations.items():
            for zipcode, clinics in zipcodes.items():
                if zipcode == "0.0":  # missing value
                    continue
                for clinic in clinics:
                    if clinic["city"] == 0.0:  # missing value
                        continue
                    city_state = ", ".join([clinic["city"].title(), state])
                    count_city_clinics[city_state] = (
                        count_city_clinics.get(city_state, 0) + 1
                    )
        return count_city_clinics

    def _construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USA country state-by-state chart.

        Author(s): Aïcha Camara
        """
        self._import_files()
        city_df = self._sort_files()

        return city_df

    def create_visual(self):
        """
        Creates the state summary chart

        Author(s): Aïcha Camara, Chanteria Milner
        """
        city_df = self._construct_data()

        fig = px.bar(city_df[-20:], x="Clinic Count", y="City", orientation="h")

        fig.update_layout(
            autosize=False,
            width=500,
            height=450,
            margin=dict(l=0, r=0, t=0, b=0),
            plot_bgcolor="#1f2630",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#E0DFDF",
        )

        fig.update_xaxes(
            linewidth=2,
            linecolor="#1c1412",
            gridcolor="#1c1412",
        )

        fig.update_yaxes(
            linewidth=2,
            linecolor="#1c1412",
        )
        fig.update_traces(marker_color="#300608")

        return fig
