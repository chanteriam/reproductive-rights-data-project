"""
This file contains the functions and functionality needed to display a State
summary of abortion-related data.
"""
import plotly.graph_objects as go
import pandas as pd
import json

from reproductive_rights_data_project.visualization.abstract_visualization import (
    Visualization,
)
from reproductive_rights_data_project.util.constants import (
    STANDARD_ENCODING,
)


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
        the visualization

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

        final_df = (
            pd.merge(
                state_df,
                gest_df[
                    ["state", "exception_life", "banned_after_weeks_since_LMP"]
                ],
                on="state",
            )
            .merge(
                insurance_df[
                    ["state", "requires_coverage", "medicaid_exception_life"]
                ],
                on="state",
            )
            .merge(
                minors_info_df[
                    [
                        "state",
                        "below_age",
                        "parental_consent_required",
                        "allows_minor_to_consent_to_abortion",
                    ]
                ],
                on="state",
            )
            .merge(
                waiting_period_df[
                    ["state", "waiting_period_hours", "counseling_visits"]
                ],
                on="state",
            )
        )

        final_df = final_df.rename(
            columns={
                "state": "State",
                "count": "Clinic Count",
                "exception_life": "Exception for Life Risk",
                "banned_after_weeks_since_LMP": "Weeks until banned",
                "requires_coverage": "Insurance Coverage?",
                "medicaid_exception_life": "Medicaid Coverage if Life Risk",
                "below_age": "Age Requirement",
                "parental_consent_required": "Parental Consent Needed?",
                "allows_minor_to_consent_to_abortion": "Can Minors Consent",
                "waiting_period_hours": "Waiting Period (Hrs)",
                "counseling_visits": "Counseling Visits",
            }
        )

        return final_df

    def construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USA country state-by-state chart.

        Author(s): Aïcha Camara
        """
        self._import_files()
        state_summary_df = self._sort_files()

        return state_summary_df

    def create_visual(self):
        """
        Creates the state summary chart

        Author(s): Aïcha Camara
        """
        state_summary_df = self.construct_data()

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=list(state_summary_df.columns),
                        fill_color="silver",
                        line_color="darkslategray",
                        align="center",
                    ),
                    cells=dict(
                        values=state_summary_df.transpose().values.tolist(),
                        fill_color="whitesmoke",
                        line_color="darkslategray",
                        align="center",
                    ),
                )
            ]
        )

        return fig
