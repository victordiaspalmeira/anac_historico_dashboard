from app import app
from dash.dependencies import Input, Output
from parsed_data import anac_df
from datetime import datetime as dt
import plotly.express as px
import re

@app.callback(
    Output('flight-duration-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph(grpname, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    
    plot_df = anac_df[anac_df['Sigla da Empresa'] == grpname]
    plot_df = plot_df.loc[str(start):str(end)]
    return px.scatter(plot_df, x=plot_df.index, y=plot_df['Chegada Prevista'], labels={"index": "Partida Prevista"})

