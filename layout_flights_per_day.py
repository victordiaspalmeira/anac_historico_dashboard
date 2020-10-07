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


layout_flights_per_day = html.Div([
    dcc.Graph('flights-per-day',  config={'displayModeBar': True})],
)


@app.callback(
    Output('flights-per-day', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flights_per_day(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, None, start, end)

    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    # plot_df_agg = plot_df[['Partida Prevista', "Situação do Voo"]].groupby(
    #     ['Partida Real']).agg('count')
    plot_df_agg = plot_df.where(
        plot_df["Situação do Voo"] == "Realizado").resample("D").count()

    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Voos por Aeorporto (Origem)")
    return px.line(plot_df_agg, x=plot_df_agg.index, y="Situação do Voo",  title="Quantidade de Voos por Dia")
