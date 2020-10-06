from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layout_departures_and_arrivals import layout_depatures_and_arrivals
from layout_flight_status import layout_flight_status
from layout_flight_duration import layout_flight_duration
from layout_flight_flight_airports_pair import layout_flight_airports_pair
from inputs import layout_inputs
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

layout_main = html.Div([layout_inputs, layout_flight_duration,
                        layout_flight_status, layout_depatures_and_arrivals, layout_flight_airports_pair])


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
    app.run_server(debug=False)
