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
app.layout = dbc.Container([
	html.Br(),
	html.Br(),
	html.Br(),    
    dbc.Row([ 
        dbc.Col([
            html.H1('Data Science Cources Among Different Universities')
        ]),
		dbc.Col([
            dbc.Row([ 
	        dbc.Button([arrow_right_icon,"All about Data Science"],
		     size = 'lg', outline = True, color="primary", className="me-1",href="/all_about_datascience"),
	    ]),
            dbc.Row([ 
                    dbc.Button([arrow_right_icon,"Industry Link"],
                    size = 'lg', outline = True, color="primary", className="me-2",href="/industry_link"),
                ]),
            dbc.Row([ 
                    dbc.Button([arrow_right_icon,"Difference between Universities"],
                    size = 'lg', outline = True, color="primary", className="me-2",href="/difference_between_universities"),
                ]),
            dbc.Row([ 
	        dbc.Button([arrow_right_icon,"Module Database"],
		     size = 'lg', outline = True, color="primary", className="me-2",href="/module_database"),
	    ]),
	    ])
    ]),
    dash.page_container
]) 


#callbacks



#run
if __name__ == '__main__':
	app.run_server(debug=True)