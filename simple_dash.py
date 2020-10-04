import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from parsed_data import anac_df

print(anac_df.index)
#dados pros dropdown
grp_empresas = anac_df['Sigla da Empresa'].unique()
grp_empresas.sort()
grp_plots = ['Duração de voo', 'Atrasos', 'Cancelados', 'Situação de Voo']

#flask
#app = dash.Dash(__name__)
#server = app.server

#elementos visuais
layout_depatures_and_arrivals = html.Div([
    html.Div([
    html.Div(
        [
            dcc.Dropdown(id='empresa-select',
                        placeholder='Empresa',
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
                    'display': 'inline-block'})]),
    html.Div([
            dcc.Input(id='data-fim', 
                    placeholder='Data de término',
                    type='text',
                    value='',
                    style={'width': '140px',
                    'display': 'inline-block'})]),
    dcc.Graph('flight-duration-plot',  config={'displayModeBar': True})])

@app.callback(
    Output('flight-duration-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('plot-select', 'value')],
    [Input('data-inicio', 'value')],
    [Input('data-fim', 'value')],

)
# Duração de Voos
# Voos Cancelados

def update_graph(empname, plotname, inicio, fim):
    start = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
    end = datetime.datetime.strptime(fim, '%d/%m/%Y').date()
    print(str(start), str(end))
    print(plotname)
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]
    
    if plotname == 'Duração de voo':
        duracao_series = (plot_df['Chegada Real'] - plot_df['Partida Real']).div(pd.Timedelta('1H'))
        return px.scatter(plot_df, x=plot_df.index, y=duracao_series, labels={"index": "Partida Prevista", "y": "Duração em horas"})
    if plotname == 'Atrasos':
        return 
    else:
        return None

