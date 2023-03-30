import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import requests
from dash import callback
from dash_iconify import DashIconify

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
dash.register_page(__name__,path='/industry_link')
arrow_back_icon = DashIconify(icon='material-symbols:line-start-arrow-rounded')
# define popup window
modal = html.Div(
    [
        dbc.Modal([
            dbc.ModalHeader("NUS-DSA"),
            dbc.ModalBody("NUS Data science course is amazing!")

        ],
            id="modal",
            size="lg",
            backdrop=True,
            is_open=False,    # True, False
            scrollable=True,  # False or True if modal has a lot of text
            centered=True,    # True, False
        ),
    ]
)
navbar = dbc.NavbarSimple(
    brand="Industry Link",
    # brand_href="#",
    color="primary",
    dark=True,
)

# Define the layout of the website
layout = html.Div([
   #html.H1('Industry Link',style={'font-size':'35px','margin-left':'10px','backgroundColor': 'lightblue'}),
    navbar,
    modal,
    # input block: 
    html.Div([
        html.H3('Key in your job description:',style={'font-size':'20px'}),
        dcc.Textarea(id='input-box',  value='',
        placeholder='Try typing SQL here',
        style={
            'font-style': 'italic', 
            'color': 'grey',
            'width':'100%',
            'height':'150px',
            'overflow-y': 'scroll'}),
        # buttons 
        html.Div([
            dbc.Button('Clear', color = 'secondary', id='clear-button'),
            dbc.Button('Search',color = 'secondary', id='search-button')
        ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-top': '10px'}),
    ],
    # overall style of LHS 
    
    style={'width': '30%', 'margin-left': '20px', 'display': 'inline-block', 'vertical-align': 'middle'}), 
    
    # output block: 
    html.Div([
        html.Div(id='output-box', 
        children=[
            html.P('Result will be shown here...', style={'text-align': 'top','font-style': 'italic', 'color': 'grey','font-size':'15px','margin-left':'10px'}),
            # html.Img(src='/assets/magnifying_glass.png', style={'display': 'block', 'margin': 'auto', 'width': '50px','height':'50px'}),
        ],
        style={'overflow-y': 'scroll', 'height': '500px','margin-top': '20px'})
    ], 
    # overall style of RHS
    style={'backgroundColor': 'lightgrey', 'width': '60%', 'display': 'inline-block', 'vertical-align': 'middle','margin-left': '60px','margin-top': '30px'}),
    dbc.Button([arrow_back_icon,"Back to Main"],
		     size = 'md', outline = True, color="primary", className="me-1",href="/"),
])


# Define the callback for the clear button to clear the input
@callback(
    [Output('input-box', 'value'),
    Output('output-box', 'children', allow_duplicate=True)],
    [Input('clear-button', 'n_clicks')],
    prevent_initial_call=True
)
def clear_input_output(n_clicks):
    if n_clicks is not None:
        return '', [html.P('Result will be shown here...', style={'text-align': 'top','font-style': 'italic', 'color': 'grey','font-size':'15px','margin-left':'10px'})]
    else:
        raise PreventUpdate


# Define the callback function that will be triggered when the user clicks the "Search" button
@callback(
    dash.dependencies.Output('output-box', 'children'),
    [dash.dependencies.Input('search-button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')]
)
def update_output(n_clicks, input_value):
    if n_clicks is not None and input_value == "SQL":
        # The user has clicked the "Search" button, so show the actual output
        output_blocks = []
        for i in range(1, 7):
            output_blocks.append(
                html.Div([
                    html.Div(str(i),
                    style={'display': 'inline-block', 'font-size':'40px','background-color': 'yellow',
                    'border-radius': '50%', 'width':'50px','height':'50px', 'text-align': 'center', 'font-weight': 'bold', 'margin': '15px'}),
                    dbc.Button(f'NUS - DSA ({10-i}0%)', color = 'secondary', id=f'school{i}-button',style={'font-size':'50px','margin-left':'15px','margin-top':'15px'})
                ])
            )
        return output_blocks
    elif n_clicks is None:
        raise PreventUpdate
    elif input_value == "":
        return [html.P('Result will be shown here...', style={'text-align': 'top','font-style': 'italic', 'color': 'grey','font-size':'15px','margin-left':'10px'})]
    else:
        return [html.P('Sorry, we cannot find any relevant information :(',style={'text-align': 'top', 'color': 'black','font-size':'20px','margin-left':'10px'})]

# callback popup window
@callback(
    Output("modal", "is_open"),
    [Input("school1-button", "n_clicks")], 
    [dash.dependencies.State("modal", "is_open")],
)
def toggle_modal(n_clicks,is_open):
    if n_clicks is not None:
        return not is_open
    return is_open 

# if __name__ == '__main__':
#     app.run_server(debug=True)