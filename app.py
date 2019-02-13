# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import glob
import os
import plotly.graph_objs as go
base_dir = os.path.dirname(os.path.abspath(__file__))
#image_directory = base_dir + '/assets/personas/'
#list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
#static_image_route = '/static/'
#print(list_of_images)
external_stylesheets = [base_dir+'/assets/main.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

data = {
        'Alexandre':{
            'Prévoyance collective': 5,
            'Mutuelle collective': 5,
            'RC Pro': 5,
            'CyberSécurité': 5,
            'Matériel - Machine': 5,
            'Protection juridique': 3,
            'Local professionnel': 3
        },
        'Laura': {
            'Prévoyance collective': 5,
            'Mutuelle collective': 5,
            'RC Pro': 5,
            'CyberSécurité': 1.5,
            'Matériel - Machine': 4,
            'Protection juridique': 4,
            'Local professionnel': 5
        },
        'Emilie': {
            'Prévoyance collective': 2.5,
            'Mutuelle collective': 4.5,
            'RC Pro': 1.5,
            'CyberSécurité': 1.5,
            'Matériel - Machine': 2,
            'Protection juridique': 1.5,
            'Local professionnel': 0
        }
}
app.layout = html.Div([
    html.Div(id='page-content'),
    dcc.Location(id='url', refresh=False),
])


index_page = html.Div([
    dcc.Link('Go to Profil de Alexandre', href='/Alexandre'),
    html.Br(),
    dcc.Link('Go to Profil de Laura', href='/Laura'),
    html.Br(),
    dcc.Link('Go to Profil de Emillie', href='/Emilie'),
])

page_1_layout = html.Div([
    dcc.Link('Go to Profil de Laura', href='/Laura'),
        html.Br(),
        dcc.Link('Go to Profil de Emillie', href='/Emilie'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
        html.H1(children='Risques Explosés'),
    html.Div([
        html.Div(
            [
                html.Img(src=app.get_asset_url('Alexandre.png'), id='personas'),
            ], style={'width':'60%', 'display':'inline-block'}
        ),
        html.Div([
            dcc.Graph(
                figure={
                    'data':[
                        go.Scatterpolar(
                            name = "Alexandre",
                            r = [val for key, val in data['Alexandre'].items()],
                            theta = [key for key, val in data['Alexandre'].items()],
                            fill = "toself",
                        ),
                    ],
                    'layout':{
                        'polar' : dict(
                        radialaxis = dict(
                            visible = True,
                            range = [i for i in range(0,10)]
                            )
                        ),
                        'showlegend' : 'True'
                    }})
    ], style={'width':'39%', 'display':'inline-block', 'margin': '0 auto'}),]),
    html.Div([
        html.Div(
            [
                html.Img(src=app.get_asset_url('Laura.png'), id='personas'),
            ],style={'width':'60%', 'display':'inline-block'}
        ),
        html.Div([
        dcc.Graph(
            figure={
                'data':[
                    go.Scatterpolar(
                        name = "Laura",
                        r = [val for key, val in data['Laura'].items()],
                        theta = [key for key, val in data['Laura'].items()],
                        fill = "toself",
                        marker = dict(
                            color='orange'
                        )
                    ),
                ],
                'layout':{
                    'polar' : dict(
                    radialaxis = dict(
                        visible = True,
                        range = [i for i in range(0,10)]
                        )
                    ),
                    'showlegend' : 'True'
                }})
    ],style={'width':'39%', 'display':'inline-block'}),]),
    html.Div([
        html.Div(
            [
                html.Img(src=app.get_asset_url('Emilie.png'), id='personas')
            ],style={'width':'60%', 'display':'inline-block'}
        ),
        html.Div([
        dcc.Graph(
            id='risk',
            figure={
                'data':[
                    go.Scatterpolar(
                        name = "Emilie",
                        r = [val for key, val in data['Emilie'].items()],
                        theta = [key for key, val in data['Emilie'].items()],
                        fill = "toself",
                        marker = dict(
                            color='green'
                        )
                    ),
                ],
                'layout':{
                    'polar' : dict(
                    radialaxis = dict(
                        visible = True,
                        range = [i for i in range(0,10)]
                        )
                    ),
                    'showlegend' : 'True'
                }})
    ],style={'width':'39%', 'display':'inline-block'}),]), 
    html.Div([
        dcc.Graph(id='synthese',
            figure={
                'data':[
                    go.Scatterpolar(
                        name = "Alexandre",
                        r = [val for key, val in data['Alexandre'].items()],
                        theta = [key for key, val in data['Alexandre'].items()],
                        fill = "toself",
                    ),
                    go.Scatterpolar(
                        name = "Laura",
                        r = [val for key, val in data['Laura'].items()],
                        theta = [key for key, val in data['Laura'].items()],
                        fill = "toself",
                    ),
                    go.Scatterpolar(
                        name = "Emilie",
                        r = [val for key, val in data['Emilie'].items()],
                        theta = [key for key, val in data['Emilie'].items()],
                        fill = "toself",
                    ),
                ],
                'layout':{
                    'polar' : dict(
                    radialaxis = dict(
                    visible = True,
                    range = [i for i in range(0,10)]
                    )
                ),
                'showlegend' : 'True'
                }
            }
        )
    ], style={'width':'50%', 'display':'inline-block', 'margin-left':'25%'})
])

page_2_layout = html.Div([
        dcc.Link('Go to Profil de Alexandre', href='/Alexandre'),
        html.Br(),
        dcc.Link('Go to Profil de Emillie', href='/Emilie'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
        html.H1(children='Risques Explosés'),
        html.Img(src=app.get_asset_url('Laura.png'), id='personas'),
        html.Br(),
        html.Br(),
        html.Br(),

])
page_3_layout = html.Div([
        dcc.Link('Go to Profil de Alexandre', href='/Alexandre'),
        html.Br(),
        dcc.Link('Go to Profil de Laura', href='/Laura'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
        html.H1(children='Risques Explosés'),
        html.Img(src=app.get_asset_url('Emilie.png'), id='personas'),
        html.Br(),
        html.Br(),
        html.Br(),

])

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Alexandre':
        return page_1_layout
    elif pathname == '/Laura':
        return page_2_layout
    elif pathname == '/Emilie':
        return page_3_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)