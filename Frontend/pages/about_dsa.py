import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import pandas as pd

#components
df = pd.read_csv('Frontend/files/about_dsa.csv')
data=df.to_dict('records')
columns=[{'id': c, 'name': c} for c in df.columns]

data

#layout
app.layout = dbc.Container([
	dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

])


#callbacks

#run
if __name__ == '__main__':
	app.run_server(debug=True)