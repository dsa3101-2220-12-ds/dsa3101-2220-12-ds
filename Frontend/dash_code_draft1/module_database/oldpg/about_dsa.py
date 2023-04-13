import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import pandas as pd

#components
dash.register_page(__name__,path='/about_dsa')

df = pd.read_csv('Frontend/files/about_dsa.csv')
data=df.to_dict('records')
columns=[{'id': c, 'name': c} for c in df.columns]
arrow_back_icon = DashIconify(icon='material-symbols:line-start-arrow-rounded')


#layout
layout = dbc.Container([
    dbc.Row(
	    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
		    style_cell={'textAlign': 'left'},
		    css=[{'selector': '.dash-cell div.dash-cell-value',
                      'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
		    style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'font-size': 25},
		    style_header={
                'backgroundColor': 'silver',
                'fontWeight': 'bold'},
		    # style_cell_conditional=[{
	        #          'if': {'col_index': 0}, 
            #              'backgroundColor': 'silver', 'fontWeight': 'bold'}],
                        
			),
	    ),
    dbc.Row([
            dbc.Col([
                dbc.Button([arrow_back_icon,"Back to Main"],
		     size = 'md', outline = True, color="primary", className="me-1",href="/"),],
             width=2
            )
        
	     ])


    

])


#callbacks

# #run
# if __name__ == '__main__':
# 	about_dsa.run_server(debug=True)
