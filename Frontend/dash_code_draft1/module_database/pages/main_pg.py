import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash


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
            [dbc.ListGroupItem(sub_option, id=f"sub-option-{option_id}-{i}", n_clicks=0, action=True) for i, sub_option in enumerate(sub_options)],
            id=f"sub-options-{option_id}",
            is_open=False,
        ),
    ])




main_layout = dbc.Container([
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
                            {"label": "Singapore University of Social Sciences (SUSS)", "value": "/suss"},
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