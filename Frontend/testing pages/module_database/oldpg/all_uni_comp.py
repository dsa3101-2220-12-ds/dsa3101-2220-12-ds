import json
import dash_cytoscape as cyto
from dash import dcc, html
from dash.dependencies import Input, Output
import dash
dash.register_page(__name__)
# Read the JSON file
with open('assets/gephi/all_uni_comp.json', 'r') as f:
    graph_data = json.load(f)

# Convert the JSON data to Cytoscape elements
elements = []
for node in graph_data['nodes']:
    elements.append({
        'data': {'id': node['id'], 'label': node['label']},
        'style': {'background-color': node['color']}
    })

for edge in graph_data['edges']:
    elements.append({
        'data': {'source': edge['source'], 'target': edge['target']}
    })


def generate_legend(color_data):
    color_groups = {}
    
    for label, color in color_data.items():
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(label)

    items = []
    for color, labels in color_groups.items():
        items.append(html.Div([
            html.Div(style={'background-color': color, 'width': '20px', 'height': '20px', 'display': 'inline-block'}),
            html.Span(", ".join(labels), style={'margin-left': '5px'})
        ], style={'margin-bottom': '5px'}))

    return items


layout = html.Div([
    html.H1('Modules Comparison across All Universities', style={'text-align': 'center'}),
    dcc.Store(id='node-colors', data={node['label']: node['color'] for node in graph_data['nodes']}),
    html.Div([
        cyto.Cytoscape(
            id='cytoscape-graph',
            elements=elements,
            layout={'name': 'cose'},
            style={'width': '75%', 'height': '800px'},
            className='cy-container',
        ),
        html.Div(id='legend-container', className='legend-container', style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'width': '25%'})
    ], style={'display': 'flex', 'flex-direction': 'row', 'align-items': 'stretch', 'justify-content': 'space-between'}),
    html.Div([
        dcc.Tabs(id='tabs', value='tab-text', children=[
            dcc.Tab(label='', value='tab-text', children=[
                html.Div([
                    html.P("This graph is a powerful tool that helps students and educators understand the relationships between data science modules from different schools in Singapore. By representing these modules as nodes and connecting them with edges, the graph provides a comprehensive overview of the entire data science curriculum.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '20px'}),
                    html.P("The main aim of the graph is to provide a visual representation of the similarities and differences between data science modules offered by various schools. It can help identify essential modules and clusters of modules, making it easier for students to plan their curriculum and choose which school is a better fit for them.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '20px'}),
                    html.P("The edges between the nodes represent the cosine similarity between modules. Cosine similarity is a mathematical measure that calculates the degree of similarity between two modules. In this graph, only modules that have a similarity score of more than 20% have edges between them. The thicker the edge, the higher the similarity score and the more similar the two modules are. Hovering your mouse over a module will show you what other modules it is similar to. This helps students and educators identify which modules are closely related based on their descriptions.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '20px'}),
                    html.P("The color of the nodes is based on the modularity of the nodes. Modularity is a term used in network analysis to group academic modules based on how similar their module descriptions are. Modules in the same modularity class are more similar to each other in terms of content and may be more closely related. Refer to the legend to see which group the module falls under! By analyzing the clusters of nodes and edges, we can identify which schools are offering similar modules. This could be useful for students looking to select courses from different schools and ensure that they are covering the necessary material.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '20px'}),
                    html.P("In addition, the graph provides valuable information on the importance of different topics across the data science curriculum. The larger the node is, the more nodes it is connected to (also known to data scientists as a higher degree!). This simply means that there are many similar modules in the entire network and it is considered an important topic for a data science curriculum, as they are found across different schools. Students can use this information to plan their curriculum effectively and ensure that they cover the essential modules.", style={'margin': 'auto', 'padding': '20px', 'fontSize': '20px'})
                    # Add more paragraphs here
                ])
            ])
        ], style={'width': '100%', 'marginTop': '20px'})
    ])
])




