"""
Creates Plotly Dash Visualization to map the cleaned data

Author(s): Aïcha Camara
"""

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# import the abstract classes for the visualizations
from src.reproductive_rights_data_project.visualization.functions import (
    read_state,
)

DASH_INSTANCE = Dash(__name__, external_stylesheets=[dbc.themes.LUX])


def build_dash(country_chart, country_map, state_map):
    """
    Author(s): Aïcha Camara, Michael Plunkett
    """
    # Creates the layout for the Plotly Dashboard
    DASH_INSTANCE.layout = html.Div(
        className="webpage",
        children=[
            html.Br(),  # html.Br() adds a line break
            html.H1(
                children="Reproductive Rights Mapping Dashboard",
                style={"textAlign": "center"},
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H4(
                        """
                        Author(s): Aïcha Camara, Kate Habich, 
                        Chanteria Milner, Michael Plunkett
                        """
                    ),
                    html.H4(
                        "If you or someone you love needs an abortion, \
                    you can find up-to-date help at ineedana.com. ❤️"
                    ),
                    html.Br(),
                ],
                style={"textAlign": "center"},
            ),
            html.Div(
                children=[
                    html.B("This box will hold the map of the United States"),
                    dcc.Graph(
                        id="usa-graph", figure=country_map.create_visual()
                    ),
                ],
                style={
                    "float": "left",
                    "height": "1020px",
                    "width": "900px",
                    "border": "1px solid black",
                    "margin": "5px",
                },
            ),
            html.Div(
                children=[
                    html.B("This box will contain the state level analyses"),
                    dcc.Graph(state_map.create_visual()),
                    dcc.Dropdown(
                        options=read_state(),
                        id="example-dropdown",
                        style={
                            "width": "500px"
                            # adds padding to the dropdown bar
                        },
                    ),
                    html.Div(id="dd-output-container"),
                ],
                style={
                    "float": "right",
                    "height": "500px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                },
            ),
            html.Div(
                children=[
                    html.B("This is where the charts will go"),
                    dcc.Graph(country_chart.create_visual()),
                ],
                style={
                    "float": "right",
                    "height": "510px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                },
            ),
        ],
    )


@DASH_INSTANCE.callback(
    Output("dd-output-container", "children"),
    Input("example-dropdown", "value"),
)
def update_output(value):
    """
    Function for the app.callback above; update_output() is a test
    function that updates the output of the navigation when another state
    is selected.
    """
    return f"{value} was selected"
