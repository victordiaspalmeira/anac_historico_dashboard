from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layout_departures_and_arrivals import layout_depatures_and_arrivals
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
        <li><a href="/departures">Horario de Partida vs Chegada</a></li>
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

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/departures':
        return layout_depatures_and_arrivals
    else:
        return None

if __name__ == '__main__':
    app.run_server(debug=False)
