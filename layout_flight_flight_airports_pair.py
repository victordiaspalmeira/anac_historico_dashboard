import pandas as pd
from datetime import datetime as dt
from app import app
from parsed_data import anac_df
from data_helpers import slice_data
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino
import numpy as np
import re
import dash


# elementos visuais
layout_flight_airports_pair = html.Div([
    dcc.Graph('flight_airports_pair',  config={'displayModeBar': True})],
)


@app.callback(
    Output('flight_airports_pair', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_airports_pair(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])

    plot_df = plot_df.loc[str(start):str(end)]

    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Aeroporto Origem vs Aeroporto Destino")
    return px.scatter(plot_df, x='Aeroporto Origem', y='Aeroporto Destino', color='Sigla da Empresa', title="Aeroporto Origem vs Aeroporto Destino")
