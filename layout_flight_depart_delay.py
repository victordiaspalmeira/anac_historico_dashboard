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
layout_flight_depart_delay = html.Div([
    dcc.Graph('flight-depart-delay-plot',  config={'displayModeBar': True})],
)

