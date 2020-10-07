from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from inputs import layout_inputs
from layout_departures_and_arrivals import *
from layout_flight_status import *
from layout_flight_type import *
from layout_flight_duration import *
from layout_flight_flight_airports_pair import *
from layout_flight_depart_delay import *
from layout_flight_arrival_delay import *
from layout_flight_status_relative import *
from layout_flights_by_airport import *
from layout_flights_per_day import *
from layout_utils import multiple_chart_div

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
        <div style="display:flex;text-align:center;justify-content:center;margin-bottom:90;">
        <p style="font-size:20px">Agência Nacional de Aviação Civil - Análise de Voos
        </p>
        </div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_main = html.Div([layout_inputs,
                        multiple_chart_div([
                            layout_flights_by_origin_airport, layout_flights_by_destination_airport]),
                        layout_flights_per_day,
                        layout_flight_duration,
                        layout_flight_depart_delay,
                        layout_flight_arrival_delay,
                        multiple_chart_div([
                            layout_flight_status, layout_flight_status_relative]),
                        layout_flight_type,
                        layout_depatures_and_arrivals,
                        layout_flight_airports_pair,
                        ])


@ app.callback(Output('page-content', 'children'),
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
        return layout_main


if __name__ == '__main__':
    app.run_server(debug=False)
