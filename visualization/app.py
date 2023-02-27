"""
Create Plotly Dash Visualization to map the cleaned data

Author(s): Aïcha Camara
"""
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# import the abstract classes for the visualizations 
from maps.usa_country import USAMap as USAMap
from maps.usa_state import USAState as USAState
from charts.state_summary import StateSummary as StateSummary

DASH_INSTANCE = Dash(__name__, external_stylesheets=[dbc.themes.LUX])


# test function for visualization
def read_state():
    """
    Test functon that reads in the states.txt data for the state dropdown
        nav bar

    Returns:
        (lst) list of states in alphabetical order
    """
    with open("./data/states.txt") as state:
        state_lst = [line.strip() for line in state.readlines()]
    return state_lst


# Create USA Figure
# def create_figure():
#     """
#     Creates the map of the United States

#     """
#     # fig = px.choropleth(data_frame, locations="state", color=, hover_name="", 
#     # locationmode='USA-states')
#     # above is to be filled in the data for the choropleth map


#     fig = go.Figure(
#         data=go.Scattergeo(
#             locations=read_state(),
#             lat=[42.3314],
#             lon=[83.0458],
#             locationmode="USA-states",
#             text="This is a marker",
#             mode="markers",
#             marker_color="black",
#         )
#     )
#     fig.update_geos(
#         visible=False,
#         resolution=110,
#         scope="usa",
#         showcountries=True,
#         countrycolor="Black",
#         showsubunits=True,
#         subunitcolor="Black",
#     )
#     fig.update_layout(height=650, margin={"r": 0, "t": 0, "l": 0, "b": 0})
#     config = {"staticPlot": True}
#     return fig


# Creates the layout for the Plotly Dashboard
DASH_INSTANCE.layout = html.Div(
    className="webpage",
    children=[
        html.Br(),  # html.Br() adds a line break
        html.H1(
            children="Test Dashboard for Reprodutive Rights Mapping",
            style={"textAlign": "center"},
        ),
        html.Div(
            children=[
                html.Br(),
                html.H4(
                    """
        This is a test to create an interactive dashboard for the Reproductive
        Rights Mapping Project
    """
                ),
                html.Br(),
            ],
            style={"textAlign": "center"},
        ),
        html.Div(
            children=[
                html.B("This box will hold the map of the United States"),
                dcc.Graph(id="usa-graph", figure=USAMap.create()),
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
                dcc.Dropdown(options=read_state(), id="example-dropdown", 
                        style={
                            "width": "500px"
                            # adds padding to the dropdown bar
                        } 
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
            children=html.B("This is where the charts will go"),
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
        function that updates the ouput of the navigation when another state
        is selected.
    """
    return f"{value} was selected"
