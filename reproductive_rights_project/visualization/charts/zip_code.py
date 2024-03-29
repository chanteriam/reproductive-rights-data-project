"""
This file contains the functions and functionality needed to render a
chart of clinics by zipcode.
"""
import json

import pandas as pd
import plotly.graph_objects as go

from reproductive_rights_project.util.constants import STANDARD_ENCODING
from reproductive_rights_project.visualization.abstract_visualization import (
    Visualization,
)
from reproductive_rights_project.visualization.util import sort_by_count


class ZipChart(Visualization):
    """
    This class represents all the methods needed to construct the zipcode chart
    in Plotly
    """

    def __init__(
        self,
        locations_file_name,
    ):

        self._locations_file_name = locations_file_name
        self._locations = None

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        with open(
            self._locations_file_name, encoding=STANDARD_ENCODING
        ) as locations:
            self._locations = json.load(locations)

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization.

        Returns (DataFrame):
            The Pandas Dataframe of abortion data by zip code.
        """

        # sorts locations data to get counts by zipcode
        count_zipcode_clinics = self._count_by_zipcode()

        # Sort by count
        count_zipcode_clinics = sort_by_count(count_zipcode_clinics)

        # create the zipcode dataframe
        zip_df = (
            pd.DataFrame.from_dict(count_zipcode_clinics, orient="index")
            .reset_index()
            .rename(columns={"index": "Zipcode", 0: "Clinic Count"})
        )
        zip_df = zip_df.sort_values(by=["Zipcode"], ascending=True)

        return zip_df

    def _count_by_zipcode(self):
        """
        This method provides a count of abortion clinics by zipcode.

        Returns (dict):
            The Dictionary containing zipcodes and clinic counts.
        """

        count_zipcode_clinics = {}
        for _, zipcodes in self._locations.items():
            for zipcode, clinics in zipcodes.items():
                if zipcode == "0.0":
                    continue
                count_zipcode_clinics[zipcode] = len(clinics)
        return count_zipcode_clinics

    def _construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USAState visual.

        Returns (DataFrame):
            The Pandas Dataframe containing zip code and clinic count data.
        """
        self._import_files()
        zip_df = self._sort_files()

        return zip_df

    def create_visual(self):
        """
        Creates the zip code level summary of clinic counts

        Returns (Figure):
            The Table representing zipcode and clinic count data.
        """

        zip_df = self._construct_data()

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=list(zip_df.columns),
                        fill_color="#300608",
                        font_color="#E0DFDF",
                        line_color="darkslategray",
                        align="center",
                    ),
                    cells=dict(
                        values=zip_df.transpose().values.tolist(),
                        fill_color=[["#c0ccd8", "#eff2f5"] * len(zip_df)],
                        line_color="darkslategray",
                        align="center",
                    ),
                )
            ]
        )

        fig.update_layout(
            autosize=False,
            width=515,
            height=500,
            margin=dict(l=0, r=0, t=0, b=0),
        )
        return fig
