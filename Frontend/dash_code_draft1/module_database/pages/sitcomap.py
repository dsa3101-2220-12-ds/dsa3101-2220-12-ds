# ntu/ntu.py
import dash_bootstrap_components as dbc
import dash_html_components as html

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1("Nanyang Technological University (NTU)", className="text-center"),
                    className="mb-5 mt-5",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Content for NTU goes here."),
                    className="mb-5",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dbc.Button(
                                "Go Back",
                                id="ntu-back-button",
                                color="primary",
                                className="mt-3",
                                href="/",
                                external_link=True,
                            )
                        ],
                        className="d-grid",
                    )
                )
            ]
        ),
    ],
    fluid=True,
)
