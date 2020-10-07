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
layout_depatures_and_arrivals = html.Div([
    dcc.Graph('flight-depart-arrival-plot',  config={'displayModeBar': True})],
)


@app.callback(
    Output('flight-depart-arrival-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_depart_arrival(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]
    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Partida e Chegada de Voos")
    return px.scatter(plot_df, y=plot_df['Chegada Real'], labels={"index": "Partida Real"}, color='Sigla da Empresa', title='Partida e Chegada de Voos')
