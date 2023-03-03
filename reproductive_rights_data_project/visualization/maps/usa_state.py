"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.
"""
import json
import pandas as pd
import plotly.graph_objects as go

from reproductive_rights_data_project.visualization.abstract_visualization import (
    Visualization,
)
from reproductive_rights_data_project.api.github.open_data_se import (
    get_state_zip_code_geo_json,
)
from reproductive_rights_data_project.visualization.functions import (
    sort_by_count,
)
from reproductive_rights_data_project.util.constants import STANDARD_ENCODING


class USAState(Visualization):
    """ "
    This class represents all the methods needed to construct the USA state map
    within plotly.

    Author(s): Aïcha Camara, Michael Plunkett
    """

    def __init__(
        self,
        gestational_info_file_name,
        insurance_info_file_name,
        locations_file_name,
        minors_info_file_name,
        waiting_period_info_file_name,
    ):
        """
        Author(s): Michael Plunkett
        """
        self._gestational_info_file_name = gestational_info_file_name
        self._gestational_info = None
        self._insurance_info_file_name = insurance_info_file_name
        self._insurance_info = None
        self._locations_file_name = locations_file_name
        self._locations = None
        self._minors_info_file_name = minors_info_file_name
        self._minors_info = None
        self._waiting_period_info_file_name = waiting_period_info_file_name
        self._waiting_period_info = None

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.

        Author(s): Aïcha Camara
        """
        with open(
            self._gestational_info_file_name, encoding=STANDARD_ENCODING
        ) as gestational, open(
            self._insurance_info_file_name, encoding=STANDARD_ENCODING
        ) as insurance, open(
            self._locations_file_name, encoding=STANDARD_ENCODING
        ) as locations, open(
            self._minors_info_file_name, encoding=STANDARD_ENCODING
        ) as minors_info, open(
            self._waiting_period_info_file_name, encoding=STANDARD_ENCODING
        ) as waiting_period:
            self._gestational_info = json.load(gestational)
            self._insurance_info = json.load(insurance)
            self._locations = json.load(locations)
            self._minors_info = json.load(minors_info)
            self._waiting_period_info = json.load(waiting_period)

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization.

        Author(s): Aïcha Camara
        """

        # set up the dataframes and standardize the orientation
        gest_df = pd.DataFrame.from_dict(
            self._gestational_info, orient="index"
        ).sort_index()
        gest_df = gest_df.reset_index().rename(columns={"index": "state"})

        insurance_df = pd.DataFrame.from_dict(
            self._insurance_info, orient="index"
        ).sort_index()
        insurance_df = insurance_df.reset_index().rename(
            columns={"index": "state"}
        )

        minors_info_df = pd.DataFrame.from_dict(
            self._minors_info, orient="index"
        ).sort_index()
        minors_info_df = minors_info_df.reset_index().rename(
            columns={"index": "state"}
        )

        waiting_period_df = pd.DataFrame.from_dict(
            self._waiting_period_info, orient="index"
        ).sort_index()
        waiting_period_df = waiting_period_df.reset_index().rename(
            columns={"index": "state"}
        )

        # sorts locations data to get counts by zipcode
        count_zipcode_clinics = {}
        for _, zipcodes in self._locations.items():
            for zipcode, clinics in zipcodes.items():
                if zipcode == "0.0":
                    continue
                count_zipcode_clinics[zipcode] = len(clinics)

        # Sort by count
        count_zipcode_clinics = sort_by_count(count_zipcode_clinics)

        # create the zipcode dataframe
        zip_df = (
            pd.DataFrame.from_dict(count_zipcode_clinics, orient="index")
            .reset_index()
            .rename(columns={"index": "zipcode", 0: "clinic count"})
        )

        # Goal: join the zipcode count dataframe and check the state that the
        # the zipcode is in

        return waiting_period_df

    def construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USAState visual.

        Author(s): Aïcha Camara
        """
        self._import_files()
        waiting_df = self._sort_files()

        return waiting_df

    def create_visual(self, state_abbrev, state_name):
        """
        Creates the map of a United States state using the data from the construct
        function and returns the plotly map of a state.

        Author(s): Aïcha Camara
        """

        """
        Note: How should we set up the callback for the state? Should the state
        name annd abbreviation be used as a parameter to then be utilized
        within this function to make a request for the geojson and then
        use that data in the visualization below? Or should another means be 
        used?
        """

        geojson = get_state_zip_code_geo_json(state_name, state_abbrev)

        test_df = self.construct_data()

        # fig = px.choropleth(state_df, #Should be indexed by the state selected!
        #                     geojson=geojson,
        #                     locations=None,
        #                     color=None,
        # )

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=list(test_df.columns),
                        fill_color="silver",
                        align="center",
                    ),
                    cells=dict(
                        values=test_df.transpose().values.tolist(),
                        fill_color="white",
                        line_color="darkslategray",
                        align="center",
                    ),
                )
            ]
        )
        return fig
