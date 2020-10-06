import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino

layout_inputs = html.Div([
    html.Div(
        [
            dcc.Dropdown(id='empresa-select',
                         options=[{'label': i, 'value': i}
                                  for i in grp_empresas],
                         placeholder='Empresa',
                         style={'width': '300px', 'margin-right': '70px'},
                         multi=True
                         ),
        ]),
    html.Div(
        [
            dcc.Dropdown(id='origem-select',
                         options=[{'label': i, 'value': i}
                                  for i in aero_origem],
                         placeholder='Origem',
                         style={'width': '140px', 'margin-right': '70px'},
                        multi=True
                         ),
        ]),
    html.Div(
        [
            dcc.Dropdown(id='destino-select',
                         options=[{'label': i, 'value': i}
                                  for i in aero_destino],
                         placeholder='Destino',
                         style={'width': '140px', 'margin-right': '70px'},
                         multi=True
                         ),
        ]),
    html.Div([
        dcc.DatePickerRange(id='periodo',
                            min_date_allowed=datetime.datetime(2015, 1, 1),
                            max_date_allowed=anac_df['Chegada Prevista'].max(
                            ),
                            start_date=datetime.datetime(2015, 1, 1),
                            end_date=datetime.datetime(2015, 1, 2),
                            style={'width': '400px',
                                   'display': 'inline-block'})])],
    style={
        'display': 'flex',
        'flex-direction': 'row',
        'flex': 1,
        'justify-content': 'center',
        'align-items': 'center'})
