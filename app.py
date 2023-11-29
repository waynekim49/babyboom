#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS 


USERNAME_PASSWORD = [['hyeongseok49','rlagudtjr49'],['kevin','kevin1234'],['hyorim1234','hyorim'],['yujin','yujin1234']]

button1 = ['혼인율','경제활동 참가비율','자치구별 출산율']
button2 = ['자치구별 1인당 GDP', '자치구별 월 평균 소득','자치구별 출산율']
button3 = ['아파트 매매가','자치구별 출산율']
button4 = ['교육 재정 지원','교육비 관련 부채 비율','교육비 관련 지출','자치구별 출산율']

app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD)
app.title = ('DashBoard | BABY BOOM')

server = app.server

app.layout = html.Div([
		html.H2('What are the factors that influence the birth rate?', # title 정의
						style = dict(textAlign = 'center',
												 marginTop = 10, # 위쪽 여백
												 marginBottom = 10 # 아래쪽 여백
												)
						),
dcc.Tabs([
        # tab 1
        dcc.Tab(label = '취업률',
                style = {'padding': '3px', 'fontWeight': 'bold',
                         'borderBottom': '1px solid #d6d6d6'},
                selected_style = {'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                                  'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'},
                children = [
                   html.Div([
                       html.P(children = '연도별: '),
                       dcc.RadioItems(id = 'radio',
                                      options = [{'label': i, 'value':i} for i in button1],
                                      value = '취업률',
                                      labelStyle = {'display': 'block'})
                   ]),
                   html.Div(className = 'Map, line',
                            children = [
                                html.Div(dcc.Graph(id = 'map1'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'map2'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'line1'),style = {'float':'left','display':'inline-block','width':'50%'}),
                                html.Div(dcc.Graph(id = 'line2'),style = {'float':'left','display':'inline-block','width':'50%'})
                ])
               ]),
        # tab 2
         dcc.Tab(label = '소득대비 출산율',
                style = {'padding': '3px', 'fontWeight': 'bold',
                         'borderBottom': '1px solid #d6d6d6'},
                selected_style = {'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                                  'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'},
                children = [
                   html.Div([
                       html.P(children = '자치구별 소득: '),
                       dcc.RadioItems(id = 'radio',
                                      options = [{'label': i, 'value':i} for i in button2],
                                      value = 'Acute Respiratory Infection',
                                      labelStyle = {'display': 'block'})
                   ]),
                   html.Div(className = 'Map, indicater',
                            children = [
                                html.Div(dcc.Graph(id = 'map3'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'map4'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'idc_jachigu1'),style = {'float':'left','width':'50%'}),
                                html.Div(dcc.Graph(id = 'idc_jachigu2'),style = {'float':'right','width':'50%'})
                ])
                                        
               ]),
         #Tab 3
          dcc.Tab(label = '부동산 매매가 대비 출산율',
                style = {'padding': '3px', 'fontWeight': 'bold',
                         'borderBottom': '1px solid #d6d6d6'},
                selected_style = {'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                                  'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'},
                children = [
                   html.Div([
                       html.P(children = '부동산 매매가: '),
                       dcc.RadioItems(id = 'radio',
                                      options = [{'label': i, 'value':i} for i in button3],
                                      value = 'Acute Respiratory Infection',
                                      labelStyle = {'display': 'block'})
                   ]),
                   html.Div(className = 'Map, indicater',
                            children = [
                               html.Div(dcc.Graph(id = 'map5'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'map6'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'idc_jachigu3'),style = {'float':'left','width':'50%'}),
                                html.Div(dcc.Graph(id = 'idc_jachigu4'),style = {'float':'right','width':'50%'})
                ])
               ]),
          #Tab 4
           dcc.Tab(label = '교육비 대비 출산율',
                style = {'padding': '3px', 'fontWeight': 'bold',
                         'borderBottom': '1px solid #d6d6d6'},
                selected_style = {'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                                  'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'},
                children = [
                   html.Div([
                       html.P(children = '교육비: '),
                       dcc.RadioItems(id = 'radio',
                                      options = [{'label': i, 'value':i} for i in button4],
                                      value = 'Acute Respiratory Infection',
                                      labelStyle = {'display': 'block'})
                   ]),
                   html.Div(className = 'Map, indicater',
                            children = [
                                html.Div(dcc.Graph(id = 'map7'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'map8'), style = {'float':'left','width': '50%','height': 650,'margin-left': 'auto','margin-right': 0}),
                                html.Div(dcc.Graph(id = 'pie1'), style = {'float':'left','display':'inline-block','width':'50%'}),
                                html.Div(dcc.Graph(id = 'pie2'), style = {'float':'left','display':'inline-block','width':'50%'})
                ])
               ])
    ])
])

# 앱 실행

if __name__=='__main__':
    app.run_server(debug = False)


# In[ ]:




