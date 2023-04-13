from dash import dcc
from dash import html
import dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash import callback
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import openpyxl
import ast

## styles ##
arrow_back_icon = DashIconify(icon='material-symbols:line-start-arrow-rounded')
dash.register_page(__name__,path='/com_btw_univ')

### data ###

# data for 6 bar charts for number of core modules by subject
df = pd.read_excel("files/salary_info.xlsx", sheet_name=2, header=0)
df_mods = df[['school.1', 'mod_cats']]

def remove_others(sch):
    """
    remove category = 'Other'; keep the rest of the categories
    """
    Subject=[]
    Number=[]
    for i in range(len(sch)):
        if sch.iloc[i,0] != 'Other':
            Subject.append(sch.iloc[i,0])
            Number.append(sch.iloc[i,1])
    dct={'Subject':Subject, 'Number of Modules': Number} 
    df = pd.DataFrame.from_dict(dct)
    return df

# make df containing subjects taught in NUS
sch_df=pd.DataFrame.from_dict(ast.literal_eval(df_mods.iloc[0,1]), orient="index").reset_index()
sch_df.columns=['Subject', 'Number of Modules']
NUS_df=pd.DataFrame(['NUS']*len(sch_df))
sch_df['School']=NUS_df

for i in range(1,len(df_mods)): # add the df other universities to NUS_df
    sch_name=df_mods.iloc[i,0]
    x = ast.literal_eval(df_mods.iloc[i,1])
    sch=pd.DataFrame.from_dict(x, orient="index").reset_index()
    sch.columns=['Subject', 'Number of Modules']
    sch=remove_others(sch)
    name_df = pd.DataFrame([sch_name]*len(sch))
    sch['School']=name_df
    sch_df = pd.concat([sch_df,sch])


# data for practical opportunities graph
df = pd.read_excel("files/salary_info.xlsx", sheet_name=2, header=0)

def make_data_opp(df):
    """
    The returned df needs to contain 3 rows for the bar chart:
    school name, percentage of modules and type of module.
    
    There should be 2 rows for each school because the type of module columns takes the value of either 'finals' or 'project'
    """
    # extract the relevant columns: 'school.1': school name, 'num_of_mods': total number of modules
    # 'mod_proj_finals': percentage of finals and project modules
    df_mods = df.loc[:,['school.1', 'num_of_mods', 'mod_proj_finals']]
    df_mods.loc[5,'mod_proj_finals'] = "{'finals':46.153846153846153846153846153846, 'proj':53.846153846153846153846153846154}"
    mods_pct = df_mods['mod_proj_finals']

    new_col=[]
    for value in mods_pct:
      dct = ast.literal_eval(value)
      school = ''
      for key,value in dct.items():
        school += str(key) + ' ' + str(value) + ' '
      new_col.append(school)

    df_mods['new_col'] = new_col
    df_mods[['Theoretical', 'val1', 'Practical', 'val2']] = df_mods['new_col'].str.split(" ", n=3, expand=True)
    df_mods_updated = pd.melt(df_mods, id_vars = ['school.1', 'val1', 'val2', 'num_of_mods'], value_vars = ['Theoretical', 'Practical'])
    df_mods_updated.loc[6:13,'val1'] = df_mods_updated.loc[6:,'val2']
    df_mods_updated = df_mods_updated[['school.1', 'val1', 'variable', 'num_of_mods']]
    df_mods_updated['val1'].astype('float')

    num_mods = []
    for i in range(len(df_mods_updated)):
      value = int(round(float(df_mods_updated.loc[i, 'val1']) * df_mods_updated.loc[i, 'num_of_mods']/100, 0))
      num_mods.append(value)
      
    df_mods_updated['num_mod_by_type'] = num_mods
    df_mods_updated['val1'] = df_mods_updated['val1'].astype('float').round(decimals=0).astype('int64')
    df_mods_updated.columns = ['School', 'Percentage', 'Type of Module', 'Total Number of Modules', 'Number of Modules']

    return df_mods_updated

data_opp = make_data_opp(df)

# data for salary graph
df = pd.read_excel("files/salary_info.xlsx", sheet_name=1, skiprows=1, header=0)
df_gross = df.loc[:,['School', 'Mean', 'Median.1', '25th Percentile', '75th Percentile']]
df_gross.loc[6,'School'] = 'SMU Cum Laude'


### make graph function ###
def make_all_bar_chart():
    fig = px.bar(sch_df, x="Subject", y="Number of Modules", color="Subject", barmode="group",
                 facet_col="School", facet_col_wrap=3,
                 color_discrete_map={'Statistics':'#f4cccc',
                                     'Mathematics':'#c9daf8',
                                     'Computer Science':'#FFD4A5',
                                     'Data Science':'#c7ebb7',
                                     'Data Analytics':'#9CE2DF'},
                 width = 1150)
    fig.update_layout(plot_bgcolor='#F8F8F8')
    fig.update_traces(marker_line=dict(width=0.5, color='Black'))
    return fig

def make_bar_chart(df):
    df = df.sort_values(by=['Percentage'], ascending=False)
    fig = px.bar(df, y="School", x="Percentage", color="Type of Module", orientation='h',
                 color_discrete_map={'Theoretical':'#c9daf8',
                                     'Practical':'#f4cccc'})
    # update graph axes and font size
    fig.update_layout(yaxis=dict(autorange='reversed'),
                      xaxis_title='Percentage of Modules',
                      yaxis_title='School',
                      plot_bgcolor='#FAFAFA')
    return fig

def make_box_plot(data):
    data=data.sort_values(by=['Mean'])

    quar1 = data['25th Percentile']
    quar3 = data['75th Percentile']
    med = data['Median.1']
    mean = data['Mean']
    schools = data['School']

    fig = go.Figure()
    fig.add_trace(go.Box(x=schools,
                         boxpoints=False,
                         median=med, mean=mean, q1=quar1, q3=quar3,
                         fillcolor='pink'))

    fig.update_layout(xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(text='School<br><br><sup>Source: MOE Graduate Employment Survey (2021) of Graduates in NUS, NTU, SMU, SIT, SUSS, SUTD</sup><br>')))
    return fig

# all graphs
default_pc = make_all_bar_chart()
salary_graph = make_box_plot(df_gross)
opp_graph = make_bar_chart(data_opp)


### app layout ###
# percentage of modules text
# source: https://towardsdatascience.com/the-3-pillars-of-math-you-need-to-know-to-become-an-effective-data-analyst-9af50106ffa1
text_graph_mod1='The series of bar charts show the number of modules offered per subject in each university.'
text_graph_mod2= 'As a prospective data science student, there are 2 important topics that you must learn - linear \
algebra (this is under Mathematics; think vectors and matrices) and Statistics. These topics will build the foundation \
for Machine Learning under the Data Science category.'
# data analytics source: https://www.mastersindatascience.org/learning/what-is-data-analytics/
text_graph_mod3 = ' There are other skills important to data scientists too - under Computer Science, you would learn \
programming languages such as Python and R, as well as SQL for database management. Under Data Analytics, you will be \
taking modules about recognising patterns in data and data visualization.'
text_graph_mod4 = 'The number of modules per subject is calculated as such:'
text_graph_list1 = 'If the module is mostly about that certain subject, the number of modules of that topic will be \
increased by 1.'
text_graph_list2 = 'If around half of a module is about that subject, the number of modules will be increased by 0.5.'

text_graph_mod5 = 'For example, in NUS, the Statistics subject has a score of 12.5. Therefore, you would expect 12.5 \
modules taken in NUS to be on the subject of Statistics.'

text_graph_mod = (html.Div(text_graph_mod1),
                  html.Br(),
                  html.Div(text_graph_mod2),
                  html.Br(),
                  html.Div(text_graph_mod3),
                  html.Br(),
                  html.Div(text_graph_mod4),
                  html.Li(text_graph_list1),
                  html.Li(text_graph_list2),
                  html.Br(),
                  html.Div(text_graph_mod5),
                  html.Br())


# salary graph text
text_graph_salary1 = 'This chart shows the mean, the median, the 25th percentile and the 75th percentile of salary \
obtained by fresh graduates in 2021.'
text_graph_salary2 = 'Do note that since the Applied Artifical Intelligence (AAI) course in SUTD was introduced \
recently and have no graduates yet, we have substituted the course with the Computer Science and Design course \
from the same university.'

text_graph_salary=(html.Div(text_graph_salary1),
                   html.Br(),
                   html.Div(text_graph_salary2))


# opportunities graph text
text_graph_opp1 = 'This chart shows the percentage of theoretical and practical modules per university.'
text_graph_opp2 = 'The theoretical modules focus more on theory which helps you understand the concept behind the \
implementation of machine learning algorithms. The practical modules focus more on coding by having more project components \
and obtaining hands-on experiences through internship modules.'
text_graph_opp3 = 'However, do  note that some practical modules may require a certain level of theoretical knowledge.'

text_graph_opp = (html.Div(text_graph_opp1),
                  html.Br(),
                  html.Div(text_graph_opp2),
                  html.Br(),
                  html.Div(text_graph_opp3))

### webpage layout ###
layout = html.Div(children=[
    html.H1(children='Differences between Universities'),
    html.Div(children=[
        dcc.Dropdown(id = 'diff_cat_dd', style={'width':280, 'font-size':18},
                     options = [{'label':'By School', 'value':'By School'}, 
                               {'label':'By Practical Opportunities', 'value':'By Practical Opportunities'},
                                {'label':'By Salary', 'value':'By Salary'}],
                     value = 'By School')
    ]),
    html.Br(),
    html.Div(children=text_graph_mod, id='text_graph', # graph description
             style={'width':'90%',
                    'font-size':18,
                    'text-align':'justify'}),
    html.Div(children=[
            dcc.Graph(id='diff_graph', figure=default_pc)],
            #style={'width':'65%'}
             ),
    dbc.Button([arrow_back_icon,"Back to Main"],
		     size = 'md', outline = True, color="primary", className="me-1",href="/"),

],
                  style = {'padding':'5px 60px'})


@callback(
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
        fig.update_layout(title='Percentage of Practical and Theoretical Modules')
    else:
        fig.update_layout(title='Number of Core Modules by Subject')
        
    return fig

@callback(
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
