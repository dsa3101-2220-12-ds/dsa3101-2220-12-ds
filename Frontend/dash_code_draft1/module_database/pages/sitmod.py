import dash
import dash_html_components as html
import base64
import os


image_filename = 'sitmod.png' # replace with your own image filename
image_path = os.path.join('assets', 'img', image_filename)
encoded_image = base64.b64encode(open(image_path, 'rb').read())

layout = html.Div([
    html.H1('SIT Modules Comparison', style={'text-align': 'center'}),
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'display': 'block', 'margin': 'auto'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


