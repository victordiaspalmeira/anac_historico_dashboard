import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino
import numpy as np

#dados pros dropdown
#flask
#app = dash.Dash(__name__)
#server = app.server

#elementos visuais
layout_flight_airports_pair = html.Div([
    dcc.Graph('flight_airports_pair',  config={'displayModeBar': True})],
)

