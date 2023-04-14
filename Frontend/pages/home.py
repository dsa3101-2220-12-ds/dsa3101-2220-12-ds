import dash
from dash import dcc
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

#components
dash.register_page(__name__,path='/')
arrow_right_icon = DashIconify(icon='material-symbols:play-arrow')

#layout
layout = dbc.Container([
	html.Br(),
	html.Br(),
	html.Br(),    
    dbc.Row([ 
        dbc.Col([
            html.H1('Data Science Courses Among Different Universities')
        ]),
		dbc.Col([
            dbc.Row([ 
	        dbc.Button([arrow_right_icon,"All about Data Science"],
		     size = 'lg', outline = True, color="primary", className="me-1",href="/about_dsa"),
	    ]),
            dbc.Row([ 
                    dbc.Button([arrow_right_icon,"Industry Link"],
                        size = 'lg', outline = True, color="primary", className="me-2",href="/industry_link",),
		                
                ]),
            dbc.Row([ 
                    dbc.Button([arrow_right_icon,"Difference between Universities"],
                        size = 'lg', outline = True, color="primary", className="me-2",href="/com_btw_univ"),
                ]),
            dbc.Row([ 
	            dbc.Button([arrow_right_icon,"Module Database"],
		            size = 'lg', outline = True, color="primary", className="me-2",href="/main"),
	            ]),
	    ])
    ]),
]) 


#callbacks



#run
# if __name__ == '__main__':
# 	app.run_server(debug=True)
