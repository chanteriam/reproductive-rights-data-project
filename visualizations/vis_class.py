from collections.abc import MutableMapping
from abc import abstractmethod


class Visualization(MutableMapping):
    @abstractmethod
    def __init__(self, filename):
        pass

    @abstractmethod
    def _import_file(self):
        """
        This method takes a JSON file and returns a dictionary of data for the \
            visualization.
        """
        pass

    @abstractmethod
    def create(self):
        """
        This method takes the dictionary made in the _import_file() method and \
            creates a visualization with it. 
        """
        pass
