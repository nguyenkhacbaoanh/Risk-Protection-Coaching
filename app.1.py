# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import glob
import os
import dash_ui as dui
import pandas as pd
import plotly.graph_objs as go

base_dir = os.path.dirname(os.path.abspath(__file__))
#image_directory = base_dir + '/assets/personas/'
#list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
#static_image_route = '/static/'
#print(list_of_images)
#external_stylesheets = [base_dir+'/assets/main.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#app.config.suppress_callback_exceptions = True

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
external_stylesheets = [base_dir+'/assets/main.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
my_css_urls = [
  "https://codepen.io/rmarren1/pen/mLqGRg.css",
]

for url in my_css_urls:
    app.css.append_css({
        "external_url": url
    })

grid = dui.Grid(_id="grid", num_rows=12, num_cols=12, grid_padding=1)

#grid.add_graph(col=1, row=1, width=5, height=5, graph_id="all-pie")

#grid.add_graph(col=6, row=1, width=7, height=10, graph_id="all-bar")

# grid.add_graph(col=1, row=6, width=5, height=5, graph_id="produce-pie")

grid.add_element(
    col=1, row=2, width=6, height=8,
    element=html.Div([
        html.H1(children='Risques Explosés'),
        html.Img(src=app.get_asset_url('Emilie.png'), id='personas')
        ], style={
            'background-color': 'Azure',
            'top': 0,
            'left': 0,
            'height':'100%',
            "text-align": "center",
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat'})
    )

# grid.add_graph(col=9, row=5, width=4, height=4, graph_id="animal-pie")

# grid.add_graph(col=1, row=9, width=9, height=4, graph_id="total-exports-bar")

# grid.add_graph(col=10, row=9, width=3, height=4, graph_id="total-exports-pie")


app.layout = html.Div(grid.get_component(), style={})

#... plot callbacks ...

if __name__ == "__main__":
    app.run_server(debug=True)