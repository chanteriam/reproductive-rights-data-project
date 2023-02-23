import pandas as pd
import plotly.graph_objects as go
from urllib.request import urlopen
from dash import Dash, html, dcc
import plotly.express as px 
import json

#def read_data()

# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)

# fig = px.choropleth( geojson=counties, locations='fips', color=None,
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 12),
#                            scope="usa",
#                            labels=None
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Black",)
fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

""""
Notes:

Formatting the data
"""