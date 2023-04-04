import dash
import dash_html_components as html
import base64
import os
import dash_core_components as dcc


image_filename = 'nusmod.png' # replace with your own image filename
image_path = os.path.join('assets', 'img', image_filename)
encoded_image = base64.b64encode(open(image_path, 'rb').read())

layout = html.Div([
    html.H1('NUS Module Comparison', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'display': 'block', 'margin': 'auto', 'max-width': '100%'})
        ], style={'width': '80%', 'display': 'inline-block', 'vertical-align': 'top'}),
        html.Div([
            dcc.Tabs(id='tabs', value='tab-text', children=[
                dcc.Tab(label='', value='tab-text', children=[
                    html.Div([
                        html.P("These filtered graphs represent the modules offered by each school, and are color-coded according to their modularity class, with edges indicating the cosine similarity between them. In other words, the edges show how similar the modules are to each other in terms of content. This information can help students understand the broad focus of each school, such as whether they have a stronger emphasis on software engineering or mathematics, or whether they offer unique modules not found in other schools.  It's important to note that the color scheme and modularity classes used in these graphs are the same as those in the larger interactive graph that includes all the schools. For more details and a more comprehensive understanding of the relationships between the modules across all schools, students are encouraged to refer to the larger graph! Overall, these filtered graphs provide a useful tool for students to explore the modules offered by each school and gain a better understanding of their respective strengths and focus areas.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '22px'})
                    ])
                ])
            ]),
        ], style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


