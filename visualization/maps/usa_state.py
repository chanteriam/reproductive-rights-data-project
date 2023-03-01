"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.

Author(s): Aïcha Camara & Michael Plunkett
"""
from abc import ABC
import pandas as pd

from visualization.abstract_visualization import Visualization
from util.constants import FILE_NAME_ABORTION_POLICY_API_GESTATION, \
FILE_NAME_ABORTION_POLICY_API_MINORS, FILE_NAME_ABORTION_POLICY_API_INSURANCE, \
FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD

class USAState(Visualization, ABC):
    def __init__(self):
        pass

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        final_dict = {}
        # above is the dicitonary with the information that will be visualized
        # fromt the API files above
        pass

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization
        """
        self._import_files()
        pass

    def create(self):
        """
        Creates the map of the United States
        """
        pass
