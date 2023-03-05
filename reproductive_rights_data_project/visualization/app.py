"""
Creates Plotly Dash Visualization to map the cleaned data

Author(s): Aïcha Camara
"""

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# import the abstract classes for the visualizations
from reproductive_rights_data_project.visualization.functions import (
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
                    html.P(
                        """
                        Author(s): Aïcha Camara, Kate Habich, 
                        Chanteria Milner, Michael Plunkett
                        """
                    ),
                    html.P(
                        "If you or someone you love needs an abortion, \
                    you can find up-to-date help at ineedana.com. ❤️"
                    ),
                    html.Br(),
                ],
                style={"textAlign": "center"},
            ),
            html.Div(
                children=[
                    html.Br(), 
                    html.H6(children=["2023 US Reproductive Rights (Hover for Information)"],
                            style={"text-align": "center"}),
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
                    dcc.Dropdown(
                        options=read_state(),
                        id="example-dropdown",
                        style={
                            "width": "500px"
                            # adds padding to the dropdown bar
                        },
                    ),
                    html.Div(id="dd-output-container"),
                    dcc.Graph(figure=state_map.create_visual())
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
                    dcc.Graph(figure=country_chart.create_visual()),
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
