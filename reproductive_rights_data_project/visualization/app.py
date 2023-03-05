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

dark_theme = {
    "main-background": "#000000",
    "header-text": "#ff7575",
    "sub-text": "#ffd175",
}


def build_dash(country_chart, country_map, state_map):
    """
    Author(s): Aïcha Camara
    """

    DASH_INSTANCE.layout = html.Div(
        className="main-div",
        children=[
            html.Br(), 
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
                    "height": "550px",
                    "width": "900px",
                    "border": "1px solid black",
                    "margin": "5px",
                    "padding-left": "1px"
                },
            ),
            html.Div(
                children=[
                    html.P(children=["Please select a state for more information"],
                            style={"text-align": "center"}),
                    dcc.Dropdown(
                        options=read_state(),
                        id="example-dropdown",
                        style={
                            #"width": "500px",
                            "padding-left": "1px",
                            "padding-right": "1px"
                            # adds padding to the dropdown bar
                        },
                    ),
                    html.Div(id="dd-output-container"), # this is where the figure will be to be updated
                    # id= usa_state_map usa_state_map(state_name="Alabama", abbrev="AL")
                    # set default with those values
                    html.Br(),
                    html.H6(children=["State Map by Zipcode (Hover for more information)"],
                            style={"text-align": "center"}),
                    dcc.Graph(figure=state_map.create_visual())
                ],
                style={
                    "float": "right",
                    "height": "550px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                    'display': 'inline-block', 
                    'vertical-align': 'middle',
                    'overflow': 'scroll'
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(children=["Clinics By Zipcode"],
                            style={"text-align": "center"})
                    #dcc.Graph(figure=country_chart.create_visual()),
                ],
                style={
                    "float": "right",
                    "height": "500px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                    'display': 'inline-block', 
                    'vertical-align': 'middle',
                    'overflow': 'scroll'
                }, 
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(children=["2023 US Reproductive Rights Chart"],
                            style={"text-align": "center"}),
                    dcc.Graph(figure=country_chart.create_visual()),
                ],
                style={
                    "float": "left",
                    "height": "500px",
                    "width": "900px",
                    "border": "1px solid black",
                    "margin": "5px",
                    'display': 'inline-block', 
                    'vertical-align': 'middle',
                    'overflow': 'scroll',
                    "padding-left": "1px"
                }
            ),
            html.Div(
        children=[
        html.Br(),
        html.P("We would like to thank the following organizations for providing our reference data: "),
        html.P("Abortion Policy API: https://www.abortionpolicyapi.com/"),
        html.P("ANSIRH Abortion Facility Database: https://abortionfacilitydatabase-ucsf.hub.arcgis.com/"),
        html.P("i need an a: https://www.ineedana.com/"),
        html.P("United States Census Bureau: https://data.census.gov/"),
        html.P("OpenDataSE: https://github.com/OpenDataDE/State-zip-code-GeoJSON"),
        html.Br()
        ],
        style={
        "text-align": "left",
        "padding-left": "5px"
        }
            )
        ],
        #style={'background-color': '#1f2630'}
        # put things here to style the main div
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
