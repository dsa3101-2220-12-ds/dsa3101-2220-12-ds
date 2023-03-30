import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

#components
app = dash.Dash(__name__, use_pages=True)
arrow_right_icon = DashIconify(icon='material-symbols:play-arrow')

#layout
app.layout = html.Div([
	html.Div("Learn more about Data Science and Analytics here!", style={'fontsize':50, 'textAlign':'center'}),
	html.Hr(),
	
    dash.page_container
    ]
)


#run
if __name__ == '__main__':
	app.run_server(debug=True)