import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State, MATCH
from dash.exceptions import PreventUpdate
import requests
from dash import callback
from dash_iconify import DashIconify
import dash_dangerously_set_inner_html

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
dash.register_page(__name__,path='/industry_link')
arrow_back_icon = DashIconify(icon='material-symbols:line-start-arrow-rounded')

schools = ['SUTD', 'NTU', 'SMU', 'SUSS', 'SIT', 'NUS']
default_message = "This popup window consists of 2 sections. You can first check the skills identified in your inputs. After that, you can check the recommended module that provides you this particular skill for each school. The score behind each module is to indicate how well this module can prepare you for this skill. Take note that the overall score is based on the distributed score for each skill. Happy reading!"
modal_content_store = {}

def get_all_response(input_value):
    response = requests.get(f"http://localhost:9001/api?input={input_value}")
    data = response.json()
    return data 

# gain mod_reco for each school 
def get_mod_reco(mod_reco,school):
    output = []
    for skill, school_info in mod_reco.items():
        module_code, score = school_info[school]
        output.append((skill,module_code,round(score,2)))
    return output 


def get_modal_content(input_value,school):
    data = get_all_response(input_value)
    if data is None:
        return None
    else:
        page = data['html_paragraph']
        mod = get_mod_reco(data['mod_reco'],school)
        return html.Div([
            html.P(default_message),
            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(page),
            html.Ul([html.Li(f"{skill}: {module_code}, {score}") for (skill, module_code, score) in mod])
        ])



# define popup window
modals = html.Div(
    [
        dbc.Modal([
                dbc.ModalHeader(f"How does the ranking work?"),
                dbc.ModalBody(id={"type": "modal-body", "index": school}, children=[])
            ],
            id={"type": "school-modal", "index": school},
            size="lg",
            backdrop=True,
            is_open=False,
            scrollable=True,
            centered=True,
        ) for school in schools
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
    modals,
    # input block: 
    html.Div([
        html.H3('Key in your job description:',style={'font-size':'20px'}),
        dcc.Textarea(id='input-box',  value='',
        placeholder='Type your job description here',
        style={
            # 'font-style': 'italic', 
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
        dcc.Loading(
            id="loading",
            children = [
                html.Div(id='output-box', 
                children=[
                    html.P('Result will be shown here...', style={'text-align': 'top','font-style': 'italic', 'color': 'grey','font-size':'15px','margin-left':'10px'}),
                ],
                style={'overflow-y': 'scroll', 'height': '500px','margin-top': '20px'})
            ],
            type = "circle",
            color="#000",)], 
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
    if input_value == "": # back to default setting 
        return [html.P('Result will be shown here...', style={'text-align': 'top','font-style': 'italic', 'color': 'grey','font-size':'15px','margin-left':'10px'})]
    elif n_clicks is not None: # as long as you have sth
        # The user has clicked the "Search" button, so show the actual output
        response = requests.get(f"http://localhost:9001/api?input={input_value}")
        data = response.json()
        scores = data["school_score"]
        sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
        output_blocks = []
        i = 1 

        # Precompute the modal content for each school and store it in the modal_content_store dictionary
        for school in schools:
            modal_content_store[school] = get_modal_content(input_value, school)

        for school, score in sorted_scores.items():
            # Since backend output do not have course name, this part is manually added. rschool = renamed school
            if school == "NUS": rschool = "NUS - Data Science and Analytics"
            elif school == "NTU": rschool = "NTU - Data Science and Artificial Intelligence"
            elif school == "SUTD": rschool = "SUTD - Computer Science and Design"
            elif school == "SIT": rschool = "SIT - Applied Artificial Intelligence"
            elif school == "SUSS": rschool = "SUSS - Business Analytics"
            else: rschool = "SMU - Economics with 2nd Major in Data Analytics"

            output_blocks.append(
                html.Div([
                    html.Div(str(i),
                    style={'display': 'inline-block', 'font-size':'30px','background-color': 'yellow',
                    'border-radius': '50%', 'width':'50px','height':'50px', 'text-align': 'center', 'font-weight': 'bold', 'margin': '15px'}),
                    dbc.Button(f'{rschool} ({round(score,2)}%)', color = 'secondary', id={'type': 'school-button', 'index': school},
                    style={'text-align': 'left','width':'80%','font-size':'30px','margin-left':'15px','margin-top':'15px'})
                ],style={'display': 'flex', 'align-items': 'center'})
            )
            i += 1 
        return output_blocks
    elif n_clicks is None:
        raise PreventUpdate

# callback popup window
@callback(
    [
        Output({"type": "school-modal", "index": MATCH}, "is_open"),
        Output({"type": "modal-body", "index": MATCH}, "children"),
    ],
    [Input({"type": "school-button", "index": MATCH}, "n_clicks")],
    [
        State({"type": "school-modal", "index": MATCH}, "is_open"),
        State("input-box", "value"),
        State({"type": "school-button", "index": MATCH}, "id")
    ],
)
def toggle_modal(n_clicks, is_open, input_value, button_id):
    if n_clicks is not None:
        school = button_id["index"]
        content = modal_content_store.get(school)
        return not is_open, content
    return is_open, []


# if __name__ == '__main__':
#     app.run_server(debug=True)
