import dash_html_components as html
import base64
import os

# First image
image_filename = 'all_uni_comp.png'
image_path = os.path.join('assets', 'img', image_filename)
encoded_image = base64.b64encode(open(image_path, 'rb').read())
img_1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'width': '60%'})

# Second image
image_filename_lg = 'all_uni_comp_lg.png'
image_path_lg = os.path.join('assets', 'img', image_filename_lg)
encoded_image_lg = base64.b64encode(open(image_path_lg, 'rb').read())
img_2 = html.Img(src='data:image/png;base64,{}'.format(encoded_image_lg.decode()), style={'width': '35%', 'float': 'right'})

# Div containing the images
images_div = html.Div(children=[img_1, img_2], style={'display': 'flex', 'flex-wrap': 'wrap'})

# Layout
layout = html.Div([
    html.H1('Modules Comparison across All Universities', style={'text-align': 'center'}),
    images_div
])
