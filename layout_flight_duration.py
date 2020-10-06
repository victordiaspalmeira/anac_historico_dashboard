import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino

#dados pros dropdown
grp_empresas = anac_df['Sigla da Empresa'].unique()
grp_empresas.sort()

#flask
#app = dash.Dash(__name__)
#server = app.server

#elementos visuais
layout_flight_duration = html.Div([
    html.Div([
    dcc.Graph('flight-duration-plot',  config={'displayModeBar': True})],
    )])
