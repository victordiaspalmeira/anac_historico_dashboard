
import dash_html_components as html


def multiple_graph_div(graphs):
    return html.Div(graphs, style={
        "flex": "1",
        "flex-direction": "row"
    })
