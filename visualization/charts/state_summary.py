"""
This file contains the functions and functionality needed to display a State
summary of abortion-related data.
"""
import plotly.graph_objects as go
import pandas as pd

from visualization.abstract_visualization import Visualization
from visualization.functions import get_zipcode_clinic_counts


class StateSummary(Visualization):
    """
    This class represents a table with information on each state.

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
        """
        return get_zipcode_clinic_counts

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization
        """
        zip_dict = self._import_files()
        zip_df = pd.DataFrame(zip_dict.items(), columns=["zip", "count"])

        return zip_df

    def construct_data(self):
        """
        Gonna update.
        """
        pass

    def create_visual(self):
        """
        Creates the state summary chart
        """
        zip_df = self._sort_files()

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=list(zip_df.columns),
                        fill_color="silver",
                        align="center",
                    ),
                    cells=dict(
                        values=zip_df.transpose().values.tolist(),
                        fill_color="white",
                        line_color="darkslategray",
                        align="center",
                    ),
                )
            ]
        )

        return fig
