from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from inputs import layout_inputs
from layout_departures_and_arrivals import *
from layout_flight_status import *
from layout_flight_type import layout_flight_type
from layout_flight_duration import layout_flight_duration, update_graph_flight_duration
from layout_flight_flight_airports_pair import *
from layout_flight_depart_delay import layout_flight_depart_delay
from layout_flight_arrival_delay import layout_flight_arrival_delay
from layout_flight_status_relative import *
from layout_utils import multiple_graph_div
import callbacks

app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Agência Nacional de Aviação Civil - Análise de Voos</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <ul>
        <li><a href="/departures">Horários de Partida vs Chegada</a></li>
        <li><a href="/status">Status de Voo</a></li>
        <li><a href="/duration">Duração de Voos</a></li>
        <li><a href="/">Índice</a></li>
        </ul>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Agência Nacional de Aviação Civil - Análise de Voos</div>
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_main = html.Div([layout_inputs,
                        layout_flight_status_relative,
                        layout_flight_duration,
                        layout_flight_depart_delay,
                        layout_flight_arrival_delay,
                        layout_flight_status,
                        layout_flight_type,
                        layout_depatures_and_arrivals,
                        layout_flight_airports_pair,
                        ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/departures':
        return layout_depatures_and_arrivals
    elif pathname == '/status':
        return layout_flight_status
    elif pathname == '/duration':
        return layout_flight_duration
    elif pathname == '/main':
        return layout_main
    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)
