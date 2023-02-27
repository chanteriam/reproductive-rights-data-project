"""
This file contains the functions and functionality needed to render a
Choropleth map of the individual States of the United States of America.
"""
from abc import ABC

from visualization.abstract_visualization import Visualization

class USAState(Visualization, ABC):
