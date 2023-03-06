"""
Creates Plotly Dash Visualization to map the cleaned data

Author(s): Aïcha Camara
"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

DASH_INSTANCE = Dash(__name__, external_stylesheets=[dbc.themes.LUX])


def build_dash(country_chart, country_map, zip_chart, city_bar):
    """
    Author(s): Aïcha Camara, Michael Plunkett
    """

    DASH_INSTANCE.layout = html.Div(
        className="main-div",
        children=[
            html.Br(),
            html.H1(
                children="Reproductive Rights Mapping Dashboard",
                style={
                    "textAlign": "center",
                    "color": "#E0DFDF",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.B(
                        "Author(s): Aïcha Camara, Kate Habich,"
                        "Chanteria Milner, Michael Plunkett"
                    ),
                    html.P(
                        "If you or someone you love needs an abortion, \
                    you can find up-to-date help at ineedana.com. ❤️"
                    ),
                    html.Br(),
                ],
                style={
                    "textAlign": "center",
                    "font-weight": "bold",
                    "color": "#E0DFDF",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(
                        children=[
                            """2023 US Reproductive Rights 
                            (Hover for " "Information) """
                        ],
                        style={
                            "text-align": "center",
                            "color": "#E0DFDF",
                        },
                    ),
                    dcc.Graph(id="usa-graph",
                              figure=country_map.create_visual()),
                ],
                style={
                    "float": "left",
                    "height": "550px",
                    "width": "900px",
                    "border": "1px solid black",
                    "margin": "5px",
                    "padding-left": "1px",
                    "color": "#E0DFDF",
                    "background": "#1f2630",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(
                        children=["Top 20 Cities by Clinic Count"],
                        style={
                            "text-align": "center",
                            "color": "#E0DFDF",
                        },
                    ),
                    html.Br(),
                    dcc.Graph(
                        figure=city_bar.create_visual(),
                        style={
                            "align": "center",
                            "justify": "center",
                            "display": "inline-block",
                            "padding-right": "10px",
                            "horizontal-align": "center",
                            "text-color": "#E0DFDF",
                        },
                    ),
                ],
                style={
                    "float": "right",
                    "height": "550px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                    "display": "inline-block",
                    "vertical-align": "middle",
                    "overflow": "scroll",
                    "background": "#1f2630",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(
                        children=["Clinics By Zipcode"],
                        style={"text-align": "center", "color": "#E0DFDF"},
                    ),
                    dcc.Graph(figure=zip_chart.create_visual()),
                ],
                style={
                    "float": "right",
                    "height": "500px",
                    "width": "515px",
                    "border": "1px solid black",
                    "margin": "5px",
                    "display": "inline-block",
                    "vertical-align": "middle",
                    "overflow": "scroll",
                    "color": "#E0DFDF",
                    "background": "#1f2630",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H6(
                        children=["2023 US Reproductive Rights Chart"],
                        style={"text-align": "center", "color": "#E0DFDF"},
                    ),
                    dcc.Graph(figure=country_chart.create_visual()),
                ],
                style={
                    "float": "left",
                    "height": "500px",
                    "width": "900px",
                    "border": "1px solid black",
                    "margin": "5px",
                    "display": "inline-block",
                    "vertical-align": "middle",
                    "overflow": "scroll",
                    "padding-left": "1px",
                    "color": "#E0DFDF",
                    "background": "#1f2630",
                },
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.P(
                        "We would like to thank the following organizations "
                        "for providing our reference data: "
                    ),
                    html.A(
                        "Abortion Policy API",
                        href="https://www.abortionpolicyapi.com/",
                        style={"color": "#b1bfce"},
                    ),
                    html.Br(),
                    html.A(
                        "ANSIRH Abortion Facility Database\t",
                        href="https://abortionfacilitydatabase-ucsf.hub.arcgis.com/",
                        style={"color": "#b1bfce"},
                    ),
                    html.Br(),
                    html.A(
                        "i need an a ❤️",
                        href="https://www.ineedana.com/",
                        style={"color": "#b1bfce"},
                    ),
                    html.Br(),
                    html.A(
                        "United States Census Bureau",
                        href="https://data.census.gov/",
                        style={"color": "#b1bfce"},
                    ),
                    html.Br(),
                    html.A(
                        "OpenDataSE",
                        href="https://github.com/OpenDataDE/State-zip-code-GeoJSON",
                        style={"color": "#b1bfce"},
                    ),
                    html.Br(),
                ],
                style={
                    "text-align": "center",
                    "padding-left": "5px",
                    "font-size": 12,
                    "color": "#b1bfce",
                },
            ),
        ],
        style={
            "background": "#1c1412",
        },
    )
