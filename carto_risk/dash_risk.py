# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
# import glob
import os
import plotly.graph_objs as go
import pandas as pd
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#image_directory = base_dir + '/assets/personas/'
#list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
#static_image_route = '/static/'
#print(list_of_images)
external_stylesheets = ['static/css/main.css']

def dash_app(server):
    app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheets)

    app.config.suppress_callback_exceptions = True

    data_risk = {
        'Alexandre': {
            'Risques': {
                'Actuel': {
                    'Matériels': {
                        'impact': 5000,
                        'fréquence': 3 
                    },
                    'Immatériels non consécultif': {
                        'impact': 5000,
                        'fréquence': 3
                    },
                    'Piratage informatique': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Diffamation': {
                        'impact': 8000,
                        'fréquence': 2
                    },
                    'Dommage système informatique': {
                        'impact': 10000,
                        'fréquence': 2
                    },
                    'Litige avec client': {
                        'impact': 5000,
                        'fréquence': 3
                    },
                    'Virus': {
                        'impact': 4000,
                        'fréquence': 3
                    },
                    'Vol avec violence': {
                        'impact': 20000,
                        'fréquence': 1
                    },
                    'Explosion, Incendie, Dommage électrique': {
                        'impact': 20000,
                        'fréquence': 1
                    },
                    'Machine': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Incendie/Explosion': {
                        'impact': 15000,
                        'fréquence': 1
                    },
                    'Dégât des eaux': {
                        'impact': 7000,
                        'fréquence': 1
                    },
                    'Arrêt du travail': {
                        'impact': 5000,
                        'fréquence': 2
                    },
                    'Optique': {
                        'impact': 2000,
                        'fréquence': 5
                    },
                    'Soins Courants': {
                        'impact': 1500,
                        'fréquence': 5
                    }
                },
                'Future': {
                    'Matériels': {
                        'impact': 5000,
                        'fréquence': 3 
                    },
                    'Immatériels non consécultif': {
                        'impact': 5000,
                        'fréquence': 3
                    },
                    'Piratage informatique': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Diffamation': {
                        'impact': 8000,
                        'fréquence': 2
                    },
                    'Dommage système informatique': {
                        'impact': 10000,
                        'fréquence': 2
                    },
                    'Litige avec client': {
                        'impact': 5000,
                        'fréquence': 3
                    },
                    'Virus': {
                        'impact': 4000,
                        'fréquence': 3
                    },
                    'Vol avec violence': {
                        'impact': 20000,
                        'fréquence': 1
                    },
                    'Explosion, Incendie, Dommage électrique': {
                        'impact': 20000,
                        'fréquence': 1
                    },
                    'Machine': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Incendie/Explosion': {
                        'impact': 15000,
                        'fréquence': 1
                    },
                    'Dégât des eaux': {
                        'impact': 7000,
                        'fréquence': 1
                    },
                    'Arrêt du travail': {
                        'impact': 10000,
                        'fréquence': 2
                    },
                    'Optique': {
                        'impact': 4000,
                        'fréquence': 5
                    },
                    'Soins Courants': {
                        'impact': 3000,
                        'fréquence': 5
                    }
                }
            }
        }
    }
    data_risk_ac = pd.DataFrame(data_risk['Alexandre']['Risques']['Actuel']).T
    data_risk_fu = pd.DataFrame(data_risk['Alexandre']['Risques']['Future']).T
    # print(data_risk['Alexandre']['Risques'].keys())
    # impact_cat = pd.cut(data_risk_df['impact'],5, labels=['ignore', 'faible', 'moyen', 'forte', 'catatrophe'])
    # impact_df = pd.qcut(data_risk_df['impact'],5)
    # print(pd.concat([impact_df,impact_cat],axis=1))
    # print(pd.concat([impact_cat,impact_df], axis=1))
    data_psycho = {
        'type': 'prudent',
        'niveau': 5
    }

    data_reserve = {
        'type': 'épargne',
        'montant': 50000
    }

    data_score = {
        'Alexandre': {
            'Actuel': {
                'Prévoyance collective': 4,
                'Mutuelle collective': 4,
                'RC Pro': 4,
                'CyberSécurité': 5,
                'Matériel - Machine': 5,
                'Protection juridique': 3,
                'Local professionnel': 3
            },
            'Future': {
                'Prévoyance collective': 5,
                'Mutuelle collective': 5,
                'RC Pro': 5,
                'CyberSécurité': 5,
                'Matériel - Machine': 5,
                'Protection juridique': 3,
                'Local professionnel': 3
            }
        },
        'Laura': {
            'Actuel': {
                'Prévoyance collective': 5,
                'Mutuelle collective': 5,
                'RC Pro': 4,
                'CyberSécurité': 1.5,
                'Matériel - Machine': 4,
                'Protection juridique': 4,
                'Local professionnel': 5
            },
            'Future': {
                'Prévoyance collective': 5,
                'Mutuelle collective': 5,
                'RC Pro': 5,
                'CyberSécurité': 1.5,
                'Matériel - Machine': 5,
                'Protection juridique': 4,
                'Local professionnel': 5
            }
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
    ])

    page_1_layout = html.Div([
        dcc.Link('Go to Profil de Laura', href='/Laura'),
            html.Br(),
            dcc.Link('Go back to home', href='/'),
            html.H1(children='Risques Explosés'),
        html.Div([
            html.Div(
                [
                    html.Img(src='static/img/Alexandre.png', id='personas'),
                ], style={'width':'60%', 'margin':'0 auto'}
            ),
            html.Div([
                dcc.RadioItems(
                    id='op',
                    options=[
                        {'label': 'Actuel', 'value': 'Actuel'},
                        {'label': 'Future', 'value': 'Future'}
                    ],
                    value='Actuel'
                ),
                dcc.Graph(id='risk')
                # dcc.Graph(
                #     figure={
                #         'data':[
                #             # go.Scatter(
                #             #     x = data_risk_fu['fréquence'],
                #             #     y = data_risk_fu['impact'], 
                #             #     mode = 'markers',
                #             #     name='future'
                #             # ),
                #             go.Scatter(
                #                 id='risk'
                #                 x = data_risk_ac['fréquence'],
                #                 y = data_risk_ac['impact'], 
                #                 mode = 'markers',
                #                 name='actuel'
                #             ),
                #         ],
                #         'layout':{
                #             'showlegend' : 'True',
                #             'xaxis':{
                #                 'tickvals':[i for i in range(1,6)],
                #                 'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                #             },
                #         }})
            ], style={'width':'39%', 'display':'inline'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data':[
                            go.Scatterpolar(
                                name = "Alexandre actuel",
                                r = [val for key, val in data_score['Alexandre']['Actuel'].items()],
                                theta = [key for key, val in data_score['Alexandre']['Actuel'].items()],
                                fill = "toself",
                            ),
                            go.Scatterpolar(
                                name = "Alexandre future",
                                r = [val for key, val in data_score['Alexandre']['Future'].items()],
                                theta = [key for key, val in data_score['Alexandre']['Future'].items()],
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
            ], style={'width':'39%', 'display':'inline'}),
        ]),
        html.Div([
            html.Div(
                [
                    html.Img(src='static/img/Laura.png', id='personas'),
                ],style={'width':'60%', 'display':'inline-block'}
            ),
            html.Div([
                dcc.Graph(
                    figure={
                        'data':[
                            go.Scatterpolar(
                                name = "Laura",
                                r = [val for key, val in data_score['Laura']['Actuel'].items()],
                                theta = [key for key, val in data_score['Laura']['Actuel'].items()],
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
    @app.callback(dash.dependencies.Output('risk', 'figure'),
    [dash.dependencies.Input('op', 'value')])
    def update_graph(option):
        if option == 'Actuel':
            return {
                    'data':[
                        # go.Scatter(
                        #     x = data_risk_fu['fréquence'],
                        #     y = data_risk_fu['impact'], 
                        #     mode = 'markers',
                        #     name='future'
                        # ),
                        go.Scatter(
                            x = data_risk_ac['fréquence'],
                            y = data_risk_ac['impact'], 
                            mode = 'markers',
                            name='actuel'
                        ),
                    ],
                    'layout':{
                        'showlegend' : 'True',
                        'xaxis':{
                            'tickvals':[i for i in range(1,6)],
                            'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                        },
                        'yaxis': {
                            'range':[0,20500],
                            'autorange':False
                        }
                    }}
        if option == 'Future':
            return {
                    'data':[
                        go.Scatter(
                            x = data_risk_fu['fréquence'],
                            y = data_risk_fu['impact'], 
                            mode = 'markers',
                            name='future'
                        ),
                        # go.Scatter(
                        #     id='risk'
                        #     x = data_risk_ac['fréquence'],
                        #     y = data_risk_ac['impact'], 
                        #     mode = 'markers',
                        #     name='actuel'
                        # ),
                    ],
                    'layout':{
                        'showlegend' : 'True',
                        'xaxis':{
                            'tickvals':[i for i in range(1,6)],
                            'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                        },
                        'yaxis': {
                            'range':[0,20500],
                            'autorange':False
                        }
                    }}
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
    return app

if __name__ == '__main__':
    app.run_server(debug=True)