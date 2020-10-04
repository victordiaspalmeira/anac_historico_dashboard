import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from parsed_data import anac_df

#dados pros dropdown
grp_empresas = anac_df['Sigla da Empresa'].unique()
grp_empresas.sort()

#flask
#app = dash.Dash(__name__)
#server = app.server

#elementos visuais
layout_depatures_and_arrivals = html.Div([
    html.Div([
    html.Div(
        [
            dcc.Dropdown(id='empresa-select', 
                        options=[{'label': i, 'value': i} for i in grp_empresas], 
                        style={'width': '140px', 'margin-right': '60px'},
                        value=grp_empresas[0]
                        ),
        ]),
    html.Div([
            dcc.DatePickerRange(id='periodo', 
                    min_date_allowed=datetime.datetime(2015, 1, 1),
                    max_date_allowed=anac_df['Chegada Prevista'].max(),
                    start_date=datetime.datetime(2015, 1, 1),
                    end_date=datetime.datetime(2019,12,31),
                    style={'width': '140px',
                    'display': 'inline-block'})])],
                    style={'display': 'flex', 'flex-direction': 'row', 'flex': 1, 'justify-content': 'center', 'align-items': 'center'}),
    dcc.Graph('flight-duration-plot',  config={'displayModeBar': True})],
    )

