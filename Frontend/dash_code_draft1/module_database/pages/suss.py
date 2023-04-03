# In nus.py
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

csv_file = "assets/Data/SUSS_course_info.csv"
df = pd.read_csv(csv_file)

categories = df["mod_category"].unique()
category_options = {
    category: [
        (str(row["mod_code"]).replace('.', '_'), row["mod_desc"])
        for _, row in df[df["mod_category"] == category][["mod_code", "mod_desc"]].iterrows()
    ]
    for category in categories
}



def main_option(option_id, title, sub_options):
    return dbc.Card([
        dbc.CardHeader(
            html.H5(
                dbc.Button(
                    title,
                    id=f"suss-main-option-{option_id}",
                    className="w-100 text-start",
                    color="link",
                )
            )
        ),
        dbc.Collapse(
            [dbc.ListGroupItem(sub_option[1], id=f"suss-sub-option-{option_id}-{i}-{sub_option[0]}", n_clicks=0, action=True) for i, sub_option in enumerate(sub_options)],
            id=f"suss-sub-options-{option_id}",
            is_open=False,
        ),
    ])


# Paste the copied layout code here, and make any modifications you need
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
                            {"label": "National University of Singapore (NUS)", "value": "/nus"},
                            {"label": "Nanyang Technological University (NTU)", "value": "/ntu"},
                            {"label": "Singapore Management University (SMU)", "value": "/smu"},
                            {"label": "Singapore University of Technology and Design (SUTD)", "value": "/sutd"},
                            {"label": "Singapore Institute of Technology (SIT)", "value": "/sit"},
                            {"label": "Choose a University", "value": "/"},
                            # Add more university options here
                        ],
                        placeholder="Singapore University of Social Sciences (SUSS)",
                        clearable=False,
                        className="select-dropdown",
                    ),
                ],
            ),

            dbc.Col([
                dcc.Link("Modules Comparison across All Universities", href="/all_uni_comp", className="rectangular-btn"),
            ], width=12),

            dbc.Col([
                dcc.Link("University Modules Comparison", href="/sussmod", className="rectangular-btn"),
            ], width=12),
        ])
    ]),

    dbc.Row([
        dbc.Col([
            main_option(option_id + 1, category, category_options[category]) for option_id, category in enumerate(categories)
        ], width=3),
        dbc.Col([
            html.Div(id="suss-content", className="content-container"),
            dcc.Link(
                html.Div("University Course Roadmap", id="circleBtn", className="circle-btn"),
                href="/susscomap",
                target="_blank",
            ),
        ], width=9),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Link("Back to Main page", href="/main", className="back-to-main-btn", style={
                "position": "absolute",
                "bottom": "0",
                "left": "0",
                "padding": "10px",
                "background-color": "#f0f0f0",  # Optional: set the background color
                "border": "1px solid black",  # Optional: set the border
            }),
        ]),
    ]),
    html.Div(id='page-content', className='content-container'),
], fluid=True)

def register_callbacks(app):
    @app.callback(
        Output("suss-content", "children"),
        [Input(f"suss-sub-option-{option_id}-{i}-{sub_option[0]}", "n_clicks") for option_id in range(1, len(categories) + 1) for i, sub_option in enumerate(category_options[categories[option_id - 1]])],
    )
    def update_content(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            return "Please select a module."

        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        module_code = input_id.split("-")[-1]

        if args[int(input_id.split("-")[-2])] == 0:
            return "Please select a module."

        module_description = df[df["mod_code"] == module_code]["mod_desc"].values[0]
        return module_description

    @app.callback(
        [Output(f"suss-sub-options-{i}", "is_open") for i in range(1, len(categories) + 1)],
        [Input(f"suss-main-option-{i}", "n_clicks") for i in range(1, len(categories) + 1)],
        [State(f"suss-sub-options-{i}", "is_open") for i in range(1, len(categories) + 1)],
    )
    def toggle_collapse(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            return [False] * len(categories)

        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        option_id = int(input_id.split("-")[-1])

        states = list(args[len(categories):])
        states[option_id - 1] = not states[option_id - 1]
        return states
