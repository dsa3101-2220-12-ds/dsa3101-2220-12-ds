from dash import dcc
from dash import html
from dash import Dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output

############ styles ##############
external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=EB+Garamond&family=Raleway:wght@500;700&display=swap'
    ]

app = Dash(__name__, external_stylesheets=external_stylesheets)

bar_chart_color = '#fff2cc'

############ data ##############
percentage_mods = {'NUS': {'CS':33, 'MA':33, 'ST':34},
                   'NTU': {'CS':40, 'MA':30, 'ST':30},
                   'SMU': {'CS':20, 'MA':50, 'ST':30},
                   'SUSS': {'CS':45, 'MA':35, 'ST':20},
                   'SUTD': {'CS':40, 'MA':40, 'ST':20},
                   'SIT': {'CS':45, 'MA':40, 'ST':15}}

df = pd.read_excel("salary_info.xlsx", sheet_name=1, skiprows=1, header=0)
df_gross = df.loc[:,['School', 'Mean', 'Median.1', '25th Percentile', '75th Percentile']]
df_gross.loc[6,'School'] = 'SMU Cum Laude'

info = {'schools':['NUS', 'NTU', 'SMU', 'SUSS', 'SIT', 'SUTD'], 'values':[38, 16, 7, 27, 0, 31]}
prac_opp_data = pd.DataFrame(data=info )

############ make graph function ##############
def make_pie_chart(school, dct):
    """
    school: string
    note: update_traces is not available for plotly version 4 and above
    """
    school_dict = dct[school]
    labels = list(school_dict.keys())
    values = list(school_dict.values())
    fig = go.Pie(values=values, labels=labels, title=school)
    fig.update(textposition='inside', textinfo='percent+label',
               marker=dict(colors=['#f4cccc', '#c9daf8', '#fff2cc']))
    return fig

def make_all_pie_chart():
    fig = make_subplots(rows=2, cols=3,
                        specs=[[{'type':'pie'}, {'type':'pie'}, {'type':'pie'}],
                               [{'type':'pie'}, {'type':'pie'}, {'type':'pie'}]])

    fig.add_trace(make_pie_chart('NUS', percentage_mods), row=1, col=1)
    fig.add_trace(make_pie_chart('NTU', percentage_mods), row=1, col=2)
    fig.add_trace(make_pie_chart('SMU', percentage_mods), row=1, col=3)
    fig.add_trace(make_pie_chart('SUSS', percentage_mods), row=2, col=1)
    fig.add_trace(make_pie_chart('SUTD', percentage_mods), row=2, col=2)
    fig.add_trace(make_pie_chart('SIT', percentage_mods), row=2, col=3)
    fig.update_layout(legend=dict(
        orientation='h', xanchor='left', yanchor='bottom', font=dict(size=14)),
                      legend_title='Module Code',
                      #height = 600, width = 900,
                      font=dict(size=14))
    return fig

def make_bar_chart(df):
    df = df.sort_values(by=['values'], ascending=False)
    schools = df['schools']
    values = df['values']
    fig = px.bar(df, x=values, y=schools) #, orientation='h')
    annotations=[] # for values beside bars

    for value, school in zip(values, schools):
        # add annotations beside bars
            annotations.append(dict(xref='x', yref='y',
                                y = school, x = value+1,
                                text=str(value),
                                showarrow=False))
    # update graph axes and font size
    fig.update_layout(yaxis=dict(autorange='reversed'),
                      annotations=annotations,
                      xaxis_title='Number of Modules',
                      yaxis_title='School',
                      font=dict(size=14),
                      plot_bgcolor='#FAFAFA')
    fig.update_traces(marker_color=bar_chart_color)
    return fig

def make_box_plot(data):
    data=data.sort_values(by=['Mean'])
    values=list(range(3200, 7500, 100))*6

    quar1 = data['25th Percentile']
    quar3 = data['75th Percentile']
    med = data['Median.1']
    mean = data['Mean']
    schools = data['School']

    box = go.Box(x=schools, name='Box Plot', boxmean=True,
                 mean=mean, median=med, q1=quar1, q3=quar3,
                 fillcolor='pink',
                 customdata=['med', 'mean'])

    layout = go.Layout(
        title='Box Plot with Mean, Median, Q1, Q3',
        yaxis=dict(title='Schools'),
        xaxis=dict(title='Salary'))

    # Create a figure object and add the box trace to it
    fig = go.Figure(data=[box], layout=layout)
    fig.update_layout(font=dict(size=14))
    return fig

def make_placeholder(dct):
    fig = px.bar(x=dct.values(), y = dct.keys(), orientation='h')
    return fig

# all graphs
default_pc = make_all_pie_chart()
salary_graph = make_box_plot(df_gross)
opp_graph = make_bar_chart(prac_opp_data)


############ app layout ##############
text_graph_mod='The series of pie charts show the differences between the number of modules offered per subject in each university.'
text_graph_salary = 'This chart here shows the mean, the median, the 25th percentile and the 75th percentile of the salary obtained by fresh graduates.'
text_graph_opp = 'This chart shows the number of modules that has project components. '

app.layout = html.Div(children=[
    html.H1(children='Differences between Universities',
            style={'font-family':'Raleway'}),
    html.Div(children=[
        dcc.Dropdown(id = 'diff_cat_dd', style={'font-family':'Raleway'},
                     options = [{'label':'By School', 'value':'By School'},
                               {'label':'By Salary', 'value':'By Salary'}, 
                               {'label':'By Practical Opportunities', 'value':'By Practical Opportunities'}],
                     value = 'By School')
    ]),    
    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id='diff_graph', figure=default_pc)],
            style={'display':'inline-block',
                   'height':'300px'}),
        html.Div(children=text_graph_mod, id='text_graph',
               style={'font-family':'Raleway',
                      'display':'inline-block',
                      'height':'100px'})])
])


@app.callback(
    Output('diff_graph', 'figure'),
    Input('diff_cat_dd', 'value')
)
def update_charts(diff_cat):
    diff_cat_title = 'By School'
    fig = default_pc

    if diff_cat == 'By Salary':
        diff_cat_title = diff_cat
        fig = salary_graph
        fig.update_layout(title='Salary of Fresh Graduates')
    elif diff_cat == 'By Practical Opportunities':
        diff_cat_title = diff_cat
        fig = opp_graph
        fig.update_layout(title='Number of Internship or Project-Based Modules')
    else:
        fig.update_layout(title='Percentage of Core Modules by Subject')
        
    return fig

@app.callback(
    Output('text_graph', 'children'),
    Input('diff_cat_dd', 'value')
    )
def update_text(diff_cat):
    diff_cat_title = 'By School'
    text = text_graph_mod

    if diff_cat == 'By Salary':
        diff_cat_title = diff_cat
        text = text_graph_salary

    elif diff_cat == 'By Practical Opportunities':
        diff_cat_title = diff_cat
        text = text_graph_opp
        
    return text

if __name__ == '__main__':
    app.run_server(debug=True)
