
import dash_html_components as html


def multiple_chart_div(charts):
    return html.Div(charts, style={
        "display": "flex",
        "flex": "1",
        "flex-direction": "row"
    })
