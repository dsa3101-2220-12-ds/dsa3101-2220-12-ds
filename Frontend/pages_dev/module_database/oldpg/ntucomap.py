import dash
import dash_html_components as html
import base64
import os
import dash_core_components as dcc
import dash
dash.register_page(__name__)

image_filename = 'ntucomap.png' # replace with your own image filename
image_path = os.path.join('assets', 'img', image_filename)
encoded_image = base64.b64encode(open(image_path, 'rb').read())

layout = html.Div([
    html.H1('NTU Course Roadmap', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'display': 'block', 'margin': 'auto', 'max-width': '100%'})
        ], style={'width': '80%', 'display': 'inline-block', 'vertical-align': 'top'}),
        html.Div([
            dcc.Tabs(id='tabs', value='tab-text', children=[
                dcc.Tab(label='', value='tab-text', children=[
                    html.Div([
                        html.P("The Pre-Requisite map for NTU provides a visual representation of how the different modules fit together in the overall curriculum. Each node on the graph represents a module, and the direction of the arrows indicates the pre-requisite relationships between them. As an incoming freshman, this graph can help you plan your course schedule by showing you which modules are required before others. The colors of the nodes represent the different levels of the modules as seen via the legend. The more arrows pointing into a module (higher in-degree) indicates that it requires many other modules as pre-requisites and is usually taken later in the degree program. The more arrows pointing out of a module (higher out-degree) indicates that it serves as an important building block for other modules in the course. Use this graph as a guide to plan your academic journey and make informed decisions about your course selections!", style={'margin': 'auto', 'padding': '20px', 'fontSize': '22px'})
                    ])
                ])
            ]),
        ], style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'})
    ])
])

# if __name__ == '__main__':
#     app.run_server(debug=True)


