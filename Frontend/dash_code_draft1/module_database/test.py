import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

def layout_main():
    layout_main = html.Div([
        html.H1('Universities Modules Database'),
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="smu"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="sit.html"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="suss"),
                ],
                className="dropdown-content",
            ),
    ])

    @app.callback(
        Output('university-link', 'children'),
        Input('university-dropdown', 'value')
    )
    def display_university_link(path):
        if path is not None:
            return dcc.Link(f'Go to {path}', href=path)

    return layout_main

        

def layout_nus():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

def layout_ntu():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

def layout_smu():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

def layout_sutd():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

def layout_sit():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

def layout_suss():
    return html.Div([
        html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="/nus"),
                    dcc.Link("Nanyang Technological University (NTU)", href="/ntu"),
                    dcc.Link("Singapore Management University (SMU)", href="/smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="/sutd"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="/sit"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="/suss"),
                ],
                className="dropdown-content",
            ),

    ])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

def display_page(pathname):
    if pathname == '/nus':
        return layout_nus()
    elif pathname == '/ntu':
        return layout_ntu()
    elif pathname == '/smu':
        return layout_smu()
    elif pathname == '/sutd':
        return layout_sutd()
    elif pathname == '/sit':
        return layout_sit()
    else:
        return layout_suss()  # Default page layout

if __name__ == '__main__':
    app.run_server(debug=True)

