import os
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

css_path = os.path.join("assets", "style.css")
external_stylesheets = [css_path]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1("Universities Modules Database"),
    html.Div([
        html.Div([
            html.Button("Option 1", className="menu-header", id="header1"),
            html.Div([
                dcc.Link("Sub-option 1A", href="page1a.html"),
                dcc.Link("Sub-option 1B", href="page1b.html"),
                dcc.Link("Sub-option 1C", href="page1c.html"),
            ], className="menu-content", id="content1"),
        ], className="menu-item"),
        html.Div([
            html.Button("Option 2", className="menu-header", id="header2"),
            html.Div([
                dcc.Link("Sub-option 2A", href="page2a.html"),
                dcc.Link("Sub-option 2B", href="page2b.html"),
                dcc.Link("Sub-option 2C", href="page2c.html"),
            ], className="menu-content", id="content2"),
        ], className="menu-item"),
        html.Div([
            html.Button("Option 3", className="menu-header", id="header3"),
            html.Div([
                dcc.Link("Sub-option 3A", href="page3a.html"),
                dcc.Link("Sub-option 3B", href="page3b.html"),
                dcc.Link("Sub-option 3C", href="page3c.html"),
            ], className="menu-content", id="content3"),
        ], className="menu-item"),
        html.Div([
            html.Button("Option 4", className="menu-header", id="header4"),
            html.Div([
                dcc.Link("Sub-option 4A", href="page4a.html"),
                dcc.Link("Sub-option 4B", href="page4b.html"),
                dcc.Link("Sub-option 4C", href="page4c.html"),
            ], className="menu-content", id="content4"),
        ], className="menu-item"),
        # Add other options similarly
    ], className="vertical-menu"),
    html.Div(id="search-result"),# Add more menu here
    
   
    dcc.Link(
        html.Div("University Course Roadmap", id="circleBtn", className="circle-btn"),
        href="roadmap.html",
        target="_blank",
    ), 
    html.Div(
        [
            html.Button("Choose a University", className="dropbtn"),
            html.Div(
                [
                    dcc.Link("National University of Singapore (NUS)", href="nus.html"),
                    dcc.Link("Nanyang Technological University (NTU)", href="ntu.html"),
                    dcc.Link("Singapore Management University (SMU)", href="smu.html"),
                    dcc.Link("Singapore University of Technology and Design (SUTD)", href="sutd.html"),
                    dcc.Link("Singapore Institute of Technology (SIT)", href="sit.html"),
                    dcc.Link("Singapore University of Social Sciences (SUSS)", href="suss.html"),
                    # Add more university links here
                ],
                className="dropdown-content",
            ),
        dcc.Link("Modules Comparison between Universities", href="umc.html", className="rectangular-btn"),

        ],
        className="dropdown",
    ),
    
    dcc.Link("Back to Main Page", href="#", className="back-btn"),
    
    html.Div(id="search-result", className="search-result"),
])


'''@app.callback(
    Output("search-result", "children"),
    [Input("circleBtn", "n_clicks"), Input("newButton", "n_clicks")],
    [dash.dependencies.State("circleBtn", "children"), dash.dependencies.State("newButton", "children")],
)
def update_search_result(circle_btn_clicks, new_btn_clicks):
    if circle_btn_clicks or new_btn_clicks:
        ctx = dash.callback_context
        if ctx.triggered:
            source = ctx.triggered[0]["prop_id"].split(".")[0]
            if source == "circleBtn":
                return "You clicked on: University Course Roadmap"
            elif source == "newButton":
                return "You clicked on: Modules Comparison between Universities"
    return None'''
@app.callback(
    [
        Output("search-result", "children"),
        Output("content1", "style"),
        Output("content2", "style"),
        Output("content3", "style"),
        Output("content4", "style"),
    ],
    [
        Input("circleBtn", "n_clicks"),
        Input("newButton", "n_clicks"),
        Input("header1", "n_clicks"),
        Input("header2", "n_clicks"),
        Input("header3", "n_clicks"),
        Input("header4", "n_clicks"),
    ],
    [
        dash.dependencies.State("circleBtn", "children"),
        dash.dependencies.State("newButton", "children"),
    ],
)
def update_search_result(
    circle_btn_clicks, new_btn_clicks, header1_clicks, header2_clicks, header3_clicks, header4_clicks
):
    ctx = dash.callback_context
    if ctx.triggered:
        source = ctx.triggered[0]["prop_id"].split(".")[0]

        if source == "circleBtn":
            return "You clicked on: University Course Roadmap", None, None, None, None
        elif source == "newButton":
            return (
                "You clicked on: Modules Comparison between Universities",
                None,
                None,
                None,
                None,
            )
        elif source.startswith("header"):
            content_id = "content" + source[-1]
            current_display = dash.callback_context.inputs[content_id + ".style"]

            new_style = {"display": "none"} if current_display["display"] == "block" else {"display": "block"}

            return (
                None,
                new_style if content_id == "content1" else None,
                new_style if content_id == "content2" else None,
                new_style if content_id == "content3" else None,
                new_style if content_id == "content4" else None,
            )
    return None, None, None, None, None

if __name__ == "__main__":
    app.run_server(debug=True)

