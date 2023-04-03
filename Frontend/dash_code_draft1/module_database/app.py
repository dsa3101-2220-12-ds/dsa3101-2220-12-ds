from dash.exceptions import PreventUpdate
from dash import Dash, html, dcc

from flask import send_from_directory
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from pages.main_pg import main_layout, register_callbacks as register_main_pg_callbacks
from pages.nus import layout as nus_layout, register_callbacks as register_nus_callbacks
from pages.ntu import layout as ntu_layout, register_callbacks as register_ntu_callbacks
from pages.smu import layout as smu_layout, register_callbacks as register_smu_callbacks
from pages.sutd import layout as sutd_layout, register_callbacks as register_sutd_callbacks
from pages.sit import layout as sit_layout, register_callbacks as register_sit_callbacks
from pages.suss import layout as suss_layout, register_callbacks as register_suss_callbacks
from pages.all_uni_comp import layout as all_uni_comp_layout
from pages.nusmod import layout as nusmod_layout
from pages.nuscomap import layout as nuscomap_layout
from pages.ntumod import layout as ntumod_layout
from pages.ntucomap import layout as ntucomap_layout
from pages.smumod import layout as smumod_layout

from pages.sutdmod import layout as sutdmod_layout

from pages.sitmod import layout as sitmod_layout

from pages.sussmod import layout as sussmod_layout



app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add the dcc.Location component
    html.Div(id='page-content'),  # Add the html.Div component
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
              
def display_page(pathname):
    if pathname == '/nus':
        return nus_layout
    elif pathname == '/ntu':
        return ntu_layout
    elif pathname == '/smu':
        return smu_layout
    elif pathname == '/sutd':
        return sutd_layout
    elif pathname == '/sit':
        return sit_layout
    elif pathname == '/suss':
        return suss_layout
    elif pathname == '/all_uni_comp':
        return all_uni_comp_layout
    elif pathname == '/nusmod':
        return nusmod_layout
    elif pathname == '/nuscomap':
        return nuscomap_layout
    elif pathname == '/ntumod':
        return ntumod_layout
    elif pathname == '/ntucomap':
        return ntucomap_layout
    elif pathname == '/smumod':
        return smumod_layout
    elif pathname == '/smucomap':
        return smucomap_layout
    elif pathname == '/sutdmod':
        return sutdmod_layout
    elif pathname == '/sutdcomap':
        return sutdcomap_layout
    elif pathname == '/sitmod':
        return sitmod_layout
    elif pathname == '/sitcomap':
        return sitcomap_layout
    elif pathname == '/sussmod':
        return sussmod_layout
    elif pathname == '/susscomap':
        return susscomap_layout
    else:
        return main_layout

'''
def init_callbacks(app: Dash):
    @app.callback(
        Output("url", "pathname"),
        Input("university-dropdown", "value"),
    )
    def update_url_pathname(selected_value):
        if selected_value:
            return selected_value
        raise PreventUpdate

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

    @app.callback(
        Output("content", "children"),
        [Input(f"sub-option-1-{j}", "n_clicks") for j in range(3)] +
        [Input(f"sub-option-2-{j}", "n_clicks") for j in range(3)] +
        [Input(f"sub-option-3-{j}", "n_clicks") for j in range(3)] +
        [Input(f"sub-option-4-{j}", "n_clicks") for j in range(3)] +
        [Input(f"sub-option-5-{j}", "n_clicks") for j in range(3)]
    )
    def update_content(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            return None
        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            option, sub_option = button_id.split('-')[2:4]
            return html.Div(f"Option {option}, Sub-option {sub_option} clicked", className="search-result-a4")

'''

@app.server.route('/assets/img/<path:path>')
def serve_image(path):
    return send_from_directory(os.path.join(app.server.static_folder, 'assets/img'), path)

register_main_pg_callbacks(app)
register_nus_callbacks(app)
register_ntu_callbacks(app)
register_smu_callbacks(app)
register_sutd_callbacks(app)
register_sit_callbacks(app)
register_suss_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)