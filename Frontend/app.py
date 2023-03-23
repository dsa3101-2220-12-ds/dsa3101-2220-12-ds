import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True)

# Define the layout of the main page
app.layout = html.Div([
    html.H1('Welcome to My Website!'),
    dcc.Link('Button 1', href='/page1'),
    html.Br(),
    dcc.Link('Button 2', href='/page2'),
    html.Br(),
    dcc.Link('Button 3', href='/page3'),
    html.Br(),
    dcc.Link('Button 4', href='/page4'),
    html.Div(id='page-content')
])

# Define the layout of page 1
page1_layout = html.Div([
    html.H1('This is Page 1'),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page3'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page4')
])

# Define the layout of page 2
page2_layout = html.Div([
    html.H1('This is Page 2'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page3'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page4')
])

# Define the layout of page 3
page3_layout = html.Div([
    html.H1('This is Page 3'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page4')
])

# Define the layout of page 4
page4_layout = html.Div([
    html.H1('This is Page 4'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page3')
])

# Define the callbacks to update the layout based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1_layout
    elif pathname == '/page2':
        return page2_layout
    elif pathname == '/page3':
        return page3_layout
    elif pathname == '/page4':
        return page4_layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
