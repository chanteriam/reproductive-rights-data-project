"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.
"""

from visualization.abstract_visualization import Visualization


class USAState(Visualization):
    """ "
    This class represents all the methods needed to construct the USA state map
    within plotly.

    Author(s): Aïcha Camara, Michael Plunkett
    """

    def __init__(self, files):
        # File names are passed from outside the class and stored in the
        # below variable
        self._files = files

    def _import_files(self):
        """
        This method accesses a JSON file(s) and returns a dictionary of data for
        the visualization.
        """
        # All files are imported here
        # This can be called within the
        return []

    def _sort_files(self):
        """
        This method utilizes the JSON file(s) to create a pandas dataframe for
        the visualization.
        """

        return []

    def construct_data(self):
        """
        This function calls and constructs the information needed to construct
        the USAState visual.
        """
        self._import_files()
        self._sort_files()

        return []

    def create_visual(self):
        """
        Creates the map of a United States state using the data from the construct
        function and returns the plotly map of a state.
        """
        return []
