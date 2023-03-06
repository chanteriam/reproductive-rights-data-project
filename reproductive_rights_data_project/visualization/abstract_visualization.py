"""
This file contains the abstract class that will be used to build all the
visualizations for this repository.
"""

from abc import ABC, abstractmethod


class Visualization(ABC):
    """
    This abstract class is the one that all visualizations will be built on.

    Author(s): Kate Habich, Michael Plunkett
    """

    @abstractmethod
    def _construct_data(self):
        """
        This method pulls and constructs all the information needed for the
        class to render the visualization.
        """
        pass

    @abstractmethod
    def create_visual(self):
        """
        This method takes the data from the _construct_data function and returns
        a visual object.
        """
        pass
