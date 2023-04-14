import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash
from dash_iconify import DashIconify
from dash import callback


arrow_back_icon = DashIconify(icon='material-symbols:line-start-arrow-rounded')
dash.register_page(__name__,path='/main')
def main_option(option_id, title, sub_options):
    return dbc.Card([
        dbc.CardHeader(
            html.H5(
                dbc.Button(
                    title,
                    id=f"main-option-{option_id}",
                    className="w-100 text-start",
                    color="link",
                )
            )
        ),
        dbc.Collapse(
            [dbc.ListGroupItem(sub_option[1], id=f"sub-option-{option_id}-{i}-{sub_option[0]}", n_clicks=0, action=True) for i, sub_option in enumerate(sub_options)],
            id=f"sub-options-{option_id}",
            is_open=False,
        ),
    ])






layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Universities Modules Database", style={"font-weight": "bold"}),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(
                [
                    dcc.Dropdown(
                        id="university-dropdown",
                        options=[
                            {"label": dcc.Link(children="National University of Singapore (NUS)" ,href="/nus"), "value": "/nus"},
                            {"label": dcc.Link(children="Nanyang Technological University (NTU)", href="/ntu"), "value": "/ntu"},
                            {"label": dcc.Link(children="Singapore Management University (SMU)", href="/smu"),"value": "/smu"},
                            {"label": dcc.Link(children="Singapore University of Technology and Design (SUTD)", href="/sutd"),"value": "/sutd"},
                            {"label": dcc.Link(children="Singapore Institute of Technology (SIT)", href="/sit"),"value": "/sit"},
                            {"label": dcc.Link(children="Singapore University of Social Sciences (SUSS)", href="/suss"),"value": "/suss"},
                            # Add more university options here
                        ],
                        placeholder="Choose a University",
                        clearable=False,
                        className="select-dropdown",
                    ),
                ],
            ),

            dbc.Col([
                dcc.Link("Modules Comparison across All Universities", href="/all_uni_comp", className="rectangular-btn"),
            ], width=12),

            dbc.Col([
                dcc.Link("University Modules Comparison", href="/nusmod", className="rectangular-btn"),
            ], width=12),
        ])
    ]),

    dbc.Row([
        dbc.Col([
            main_option(1, "Option 1", ["Sub-option 1.1", "Sub-option 1.2", "Sub-option 1.3"]),
            main_option(2, "Option 2", ["Sub-option 2.1", "Sub-option 2.2", "Sub-option 2.3"]),
            main_option(3, "Option 3", ["Sub-option 3.1", "Sub-option 3.2", "Sub-option 3.3"]),
            main_option(4, "Option 4", ["Sub-option 4.1", "Sub-option 4.2", "Sub-option 4.3"]),
            main_option(5, "Option 5", ["Sub-option 5.1", "Sub-option 5.2", "Sub-option 5.3"]),
        ], width=3),
        dbc.Col([
            html.Div(id="content", className="content-container"),
            dcc.Link(
                html.Div("University Course Roadmap", id="circleBtn", className="circle-btn"),
                href="/nuscomap",
                target="_blank",
            ),
        ], width=9),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Button([arrow_back_icon,"Back to Main"],
		     size = 'md', outline = True, color="primary", className="me-1",href="/"),
        ]),
    ]),
    html.Div(id='page-content', className='content-container'),
], fluid=True)

def register_callbacks(app: Dash):
    @app.callback(
        Output("url", "pathname"),
        Input("university-dropdown", "value"),
    )
    def update_url_pathname(selected_value):
        if selected_value:
            return selected_value
        raise dash.exceptions.PreventUpdate

    @app.callback(
        [Output(f"sub-options-{i}", "is_open") for i in range(1, 6)],
        [Input(f"main-option-{i}", "n_clicks") for i in range(1, 6)],
        [dash.dependencies.State(f"sub-options-{i}", "is_open") for i in range(1, 6)],
    )
    def toggle_sub_options(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            return [False] * 5
        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            index = int(button_id.split("-")[-1]) - 1
            state_values = args[len(args)//2:]
            new_states = [not state_values[index] if i == index else False for i in range(len(state_values))]
            return new_states
        

# @callback(Output("url", "pathname"), Input("page_dd", "value"))
# def update_url_on_dropdown_change(dropdown_value):
#     return dropdown_value
