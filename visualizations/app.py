import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

def read_state():
    with open("/Users/necabotheking/Documents/Github/reproductive-rights-data-project/data/states.txt") as state:
        state_lst = [line.strip() for line in state.readlines()]
    return state_lst


# Create Test Figure
def create_figure():
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        visible=False, resolution=110, scope="usa",
        showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Black",)
    fig.update_layout(height=650, margin={"r":0,"t":0,"l":0,"b":0})
    config = {'staticPlot': True}
    return fig

# Creates the layout for the Plotly Dashboard
app.layout = html.Div(children=[
    html.H1(children='Test Dashboard'),

    html.Div(children='''
        This is a test to create an interactive dashboard for the Reproductive
        Rights Mapping Project
    '''),
    
    # Add the dropdown with the states in alphabetical order
    dcc.Dropdown(options=read_state(), id="example-dropdown"),
    html.Div(id='dd-output-container'),

    dcc.Graph(
        id='usa-graph',
        figure=create_figure()
    )
])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('example-dropdown', 'value')
)
def update_output(value):
    return f"{value} was selected"

if __name__ == '__main__':
    app.run_server(host='localhost',port=8005)
