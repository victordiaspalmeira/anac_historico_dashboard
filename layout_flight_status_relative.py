from app import app
from parsed_data import anac_df
from data_helpers import slice_data
from datetime import datetime as dt
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino
import numpy as np
import re
import dash


layout_flight_status_relative = html.Div([
    dcc.Graph('flight-status-plot-relative',  config={'displayModeBar': True})],
    style={"flex": "1"})


@app.callback(
    Output('flight-status-plot-relative', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_status_relative(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)

    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    plot_df_all = plot_df[['Sigla da Empresa', 'Situação do Voo']].groupby(
        ['Sigla da Empresa']).agg('count')
    plot_df_canceled = plot_df[['Sigla da Empresa', 'Situação do Voo']].where(
        plot_df['Situação do Voo'] == 'Cancelado').groupby(['Sigla da Empresa']).agg('count')
    inner_join = pd.merge(left=plot_df_all, right=plot_df_canceled,
                          left_on='Sigla da Empresa', right_on='Sigla da Empresa')
    inner_join.columns = ['Total', 'Cancelados']
    inner_join['Relativo'] = inner_join['Cancelados'] / inner_join['Total']

    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Situação do Voo")

    return px.bar(inner_join, y='Relativo', title="Porcentagem de Voos Cancelados por Empresa", hover_data=["Relativo", "Total"])
