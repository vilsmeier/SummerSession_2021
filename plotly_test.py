# import plotly

# plotly.tools.set_credentials_file(
#     username='Vilsemeier',       # 账户名
#     api_key='yoQsFRbXbslvPoh8rQtw'              # api key
# )


import dash
# from gevent import pywsgi
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, meta_tags=[{"name" :"viewport","content" :"width=device-width, initial-scale=1"}], 
                external_stylesheets=external_stylesheets)




zzz = 0
for i in range(1000000000000000):
    if i%10000000==0:
        zzz = i/10000000
        print(zzz)

        app.run_server(debug=False,port=8060)



        # assume you have a "long-form" data frame
        # see https://plotly.com/python/px-arguments/ for more options
        df = pd.DataFrame({
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 8, 1, 6, 3, zzz],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })

        fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),
            html.Div(children='''Dash: A web application framework for Python.'''),
            dcc.Graph(
                id='example-graph',
                figure=fig
            )
        ])



# app.run_server(debug=False,port=8060)
