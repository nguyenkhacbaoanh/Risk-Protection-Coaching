# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent
# import glob
import os
import plotly.graph_objs as go
import pandas as pd
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#image_directory = base_dir + '/assets/personas/'
#list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
#static_image_route = '/static/'
#print(list_of_images)
external_stylesheets = ['static/css/main.css', \
'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',\
'https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css',\
'https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css']
# print(helpq(go.Table))
def dash_app(server):
    app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheets)

    app.config.suppress_callback_exceptions = True

    data_risk = {
        'Alexandre': {
            'Risques': {
                'Actuel': {
                    'Matériels': {
                        'impact': 4000,
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
                        'impact': 12000,
                        'fréquence': 2
                    },
                    'Litige avec client': {
                        'impact': 6500,
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
                        'impact': 18000,
                        'fréquence': 1
                    },
                    'Machine': {
                        'impact': 11000,
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
                        'impact': 6000,
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
                        'impact': 4000,
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
                        'impact': 12000,
                        'fréquence': 2
                    },
                    'Litige avec client': {
                        'impact': 6500,
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
                        'impact': 18000,
                        'fréquence': 1
                    },
                    'Machine': {
                        'impact': 11000,
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
                        'impact': 9000,
                        'fréquence': 2
                    },
                    'Optique': {
                        'impact': 6600,
                        'fréquence': 5
                    },
                    'Soins Courants': {
                        'impact': 5700,
                        'fréquence': 5
                    }
                }
            }
        },
        'Laura': {
            'Risques': {
                'Actuel': {
                    'Accident du travail': {
                        'impact': 3000,
                        'fréquence': 5
                    },
                    'endommagé du bien': {
                        'impact': 1000,
                        'fréquence': 5
                    },
                    'dommage le système informatique': {
                        'impact': 1500,
                        'fréquence': 3
                    },
                    'dommage le logiciel d\'acheté': {
                        'impact': 4000,
                        'fréquence': 3,
                    },
                    'les conflits inviduelle de travail': {
                        'impact': 3000,
                        'fréquence': 5,
                    },
                    'les conflits avec clients': {
                        'impact': 10000,
                        'fréquence': 5
                    },
                    'Incendie': {
                        'impact': 20000,
                        'fréquence': 2
                    },
                    'Explosion': {
                        'impact': 20000,
                        'fréquence': 2
                    },
                    'Dégât des eaux': {
                        'impact': 8000,
                        'fréquence': 2
                    },
                    'Machines': {
                        'impact': 8000,
                        'fréquence': 3
                    },
                    'Vol': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Arrêt de travail': {
                        'impact': 2000,
                        'fréquence': 5
                    },
                    'Soins courants': {
                        'impact': 5000,
                        'fréquence': 5
                    }
                },
                'Future': {
                    'Accident du travail': {
                        'impact': 6000,
                        'fréquence': 5
                    },
                    'endommagé du bien': {
                        'impact': 1000,
                        'fréquence': 5
                    },
                    'dommage le système informatique': {
                        'impact': 1500,
                        'fréquence': 3
                    },
                    'dommage le logiciel d\'acheté': {
                        'impact': 4000,
                        'fréquence': 3,
                    },
                    'les conflits inviduelle de travail': {
                        'impact': 5000,
                        'fréquence': 5,
                    },
                    'les conflits avec clients': {
                        'impact': 12000,
                        'fréquence': 5
                    },
                    'Incendie': {
                        'impact': 20000,
                        'fréquence': 2
                    },
                    'Explosion': {
                        'impact': 20000,
                        'fréquence': 2
                    },
                    'Dégât des eaux': {
                        'impact': 8000,
                        'fréquence': 2
                    },
                    'Machines': {
                        'impact': 8000,
                        'fréquence': 3
                    },
                    'Vol': {
                        'impact': 10000,
                        'fréquence': 1
                    },
                    'Arrêt de travail': {
                        'impact': 6000,
                        'fréquence': 5
                    },
                    'Soins courants': {
                        'impact': 8000,
                        'fréquence': 5
                    }
                }
            }
        }
    }
    data_risk_ac = pd.DataFrame(data_risk['Alexandre']['Risques']['Actuel']).T
    data_risk_fu = pd.DataFrame(data_risk['Alexandre']['Risques']['Future']).T
    data_risk_ac_Laura = pd.DataFrame(data_risk['Laura']['Risques']['Actuel']).T
    data_risk_fu_Laura = pd.DataFrame(data_risk['Laura']['Risques']['Future']).T
    # print(data_risk_ac.index)
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
        # html.Div(id='page-content'),
        # dcc.Location(id='url', refresh=False),
        dcc.Tabs(id="tabs", value='alexandre', children=[
        dcc.Tab(label='Alexandre', value='alexandre'),
        dcc.Tab(label='Laura', value='laura'),
        ]),
        html.Div(id='page-content')
    ])


    page_1_layout = html.Div([
        html.H4("Profile de Alexandre", style={'background-color':'rgba(256,0,0,0.6)','text-align':'center'}),
        html.Div([
                html.Img(src='static/img/Alexandre.png', id='personas'),
            ], style={'width':'60%', 'margin':'0 auto'}
        ),
        html.H4("Cartographique des risques", style={'background-color':'rgba(256,0,0,0.6)','text-align':'center'}),
        html.Div([
            # html.Button('Print PDF',id="button-print",style={'position': "absolute", 'top': '50', 'right': '0'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [
                            go.Table(
                                columnorder = [1,2],
                                columnwidth = [20,40],
                                header = dict(
                                    values=[['Impact']],
                                    height=40,
                                    line = dict(color = '#506784'),
                                    fill = dict(color = '#119DFF'),
                                    align = ['left','center'],
                                    font = dict(color = 'white', size = 12),
                                ),
                                cells = dict(
                                    values=[
                                        ['très significatif', 'Majeur', 'Modéré', 'Mineur', 'Non significatif'],\
                                        ['> 20M €', '15M € à 20M €', '10M € à 15M €', '5M € à 10M €', '< 5M €']
                                        ],
                                    line = dict(color = '#506784'),
                                    fill = dict(color = ['#25FEFD', 'white']),
                                    align = ['left', 'center'],
                                    font = dict(color = '#506784', size = 12),
                                )

                            )
                        ]
                    }
                )
            ], style={'width':'25%', 'display':'inline-block'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data':[
                            go.Scatter(
                                # id='risk',
                                x = data_risk_ac['fréquence'],
                                y = data_risk_ac['impact'],
                                mode = 'markers+text',
                                text = [i for i in range(1, data_risk_ac.shape[0]+1)],
                                textposition='top right',
                                name='actuel',
                                marker = {
                                    'color': 'green'
                                },
                                hoverinfo = 'x+y+text'
                            ),
                        ],
                        'layout':{
                            'title':'Alexandre Actuel',
                            'showlegend' : 'True',
                            'xaxis':{
                                'title': 'Fréquence',
                                'tickvals':[i for i in range(1,6)],
                                'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                            },
                            'hovermode':'closest',
                            'hoverlabel': {
                                'bgcolor':'violet',
                                'font': {
                                    'color': 'black'
                                }
                            }
                        }})
            ], style={'width':'49%', 'display':'inline-block'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [
                            go.Table(
                                columnorder = [1,2],
                                columnwidth = [20,40],
                                header = dict(
                                    values=[[''],['Risques']],
                                    height=40,
                                    line = dict(color = '#506784'),
                                    fill = dict(color = '#119DFF'),
                                    align = ['left','center'],
                                    font = dict(color = 'white', size = 12),
                                ),
                                cells = dict(
                                    values=[
                                        [i for i in range(1,len(data_risk_ac)+1)],
                                        [i for i in data_risk_ac.index]
                                        ],
                                    line = dict(color = '#506784'),
                                    fill = dict(color = ['#25FEFD', 'white']),
                                    align = ['left', 'center'],
                                    font = dict(color = '#506784', size = 12),
                                )

                            )
                        ],
                        'layout': {
                            'scrollmode': False
                        }
                    }
                )
            ], style={'width':'25%', 'display':'inline-block', 'margin-right':'0px'}),
            html.Div([
                html.Div([
                    # dcc.Markdown(dedent('''
                    # ## Alexandre Future
                    # ''')),
                    dcc.Graph(
                        figure={
                            'data':[
                                go.Scatter(
                                    x = data_risk_fu['fréquence'],
                                    y = data_risk_fu['impact'], 
                                    mode = 'markers+text',
                                    text = [i for i in range(1, data_risk_ac.shape[0]+1)],
                                    textposition='top right',
                                    name='future',
                                    marker = {
                                        'color': 'red'
                                    }
                                ),
                            ],
                            'layout':{
                                'title':'Alexandre Future',
                                'showlegend' : 'True',
                                'xaxis':{
                                    'title': 'Fréquence',
                                    'tickvals':[i for i in range(1,6)],
                                    'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                                },
                                'hovermode':'closest',
                                'hoverlabel': {
                                    'bgcolor':'violet',
                                    'font': {
                                        'color': 'black'
                                    }
                                }
                            }})
                ], style={'width':'70%', 'display':'inline-block'}),
            ],style={'margin-left':'20%'}),
            html.Div([
                dcc.Markdown(dedent('''
                Alexandre a fait face aux risques concernés Yeux (Optiques), Soins courants car il veux recruter des salariés
                '''))], style={'display':'inline-block', 'margin-left':'20%'}
            ),
            html.H4("Risques potentiels", style={'background-color':'rgba(256,0,0,0.6)','text-align':'center'}),
            html.Div([
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Risques faibles</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Risques forts</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ],style={'width':'39%', 'display':'inline-block', 'margin-top':'20px', 'margin-left':'35%'}),
            html.H4("La proposition au niveau de protection", style={'background-color':'rgba(256,0,0,0.6)','text-align':'center'}),
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
                            'title': 'Les risques correspondent aux offres d\'assurances',
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
        
    ])

    page_2_layout = html.Div([
            html.H4('Profil de Laura', style={'background-color':'rgba(256,0,0,0.6)', 'text-align':'center'}),
            html.Div(
                [
                    html.Img(src='static/img/Laura.png', id='personas'),
                ], style={'width':'60%', 'margin':'0 auto'}
            ),
            html.H4('Cartographique des risques', style={'background-color':'rgba(256,0,0,0.6)', 'text-align':'center'}),
            html.Div([
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [
                            go.Table(
                                columnorder = [1,2],
                                columnwidth = [20,40],
                                header = dict(
                                    values=[['Impact']],
                                    height=40,
                                    line = dict(color = '#506784'),
                                    fill = dict(color = '#119DFF'),
                                    align = ['left','center'],
                                    font = dict(color = 'white', size = 12),
                                ),
                                cells = dict(
                                    values=[
                                        ['très significatif', 'Majeur', 'Modéré', 'Mineur', 'Non significatif'],\
                                        ['> 20M €', '15M € à 20M €', '10M € à 15M €', '5M € à 10M €', '< 5M €']
                                        ],
                                    line = dict(color = '#506784'),
                                    fill = dict(color = ['#25FEFD', 'white']),
                                    align = ['left', 'center'],
                                    font = dict(color = '#506784', size = 12),
                                )

                            )
                        ]
                    }
                )
            ], style={'width':'25%', 'display':'inline-block'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data':[
                            # go.Scatter(
                            #     x = data_risk_fu['fréquence'],
                            #     y = data_risk_fu['impact'], 
                            #     mode = 'markers',
                            #     name='future'
                            # ),
                            go.Scatter(
                                # id='risk',
                                x = data_risk_ac_Laura['fréquence'],
                                y = data_risk_ac_Laura['impact'],
                                mode = 'markers+text',
                                text = [i for i in range(1, data_risk_ac_Laura.shape[0]+1)],
                                textposition='top right',
                                name='actuel',
                                marker = {
                                    'color': 'green'
                                },
                                hoverinfo = 'x+y+text'
                            ),
                        ],
                        'layout':{
                            'title':'Laura Actuel',
                            'showlegend' : 'True',
                            'xaxis':{
                                'title': 'Fréquence',
                                'tickvals':[i for i in range(1,6)],
                                'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                            },
                            'hovermode':'closest',
                            'hoverlabel': {
                                'bgcolor':'violet',
                                'font': {
                                    'color': 'black'
                                }
                            }
                        }})
            ], style={'width':'49%', 'display':'inline-block'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [
                            go.Table(
                                columnorder = [1,2],
                                columnwidth = [20,40],
                                header = dict(
                                    values=[[''],['Risques']],
                                    height=40,
                                    line = dict(color = '#506784'),
                                    fill = dict(color = '#119DFF'),
                                    align = ['left','center'],
                                    font = dict(color = 'white', size = 12),
                                ),
                                cells = dict(
                                    values=[
                                        [i for i in range(1,len(data_risk_ac_Laura)+1)],
                                        [i for i in data_risk_ac_Laura.index]
                                        ],
                                    line = dict(color = '#506784'),
                                    fill = dict(color = ['#25FEFD', 'white']),
                                    align = ['left', 'center'],
                                    font = dict(color = '#506784', size = 12),
                                )

                            )
                        ],
                        'layout': {
                            'scrollmode': False
                        }
                    }
                )
            ], style={'width':'25%', 'display':'inline-block', 'margin-right':'0px'}),
            html.Div([
                html.Div([
                    # dcc.Markdown(dedent('''
                    # ## Alexandre Future
                    # ''')),
                    dcc.Graph(
                        figure={
                            'data':[
                                go.Scatter(
                                    x = data_risk_fu_Laura['fréquence'],
                                    y = data_risk_fu_Laura['impact'], 
                                    mode = 'markers+text',
                                    text = [i for i in range(1, data_risk_ac_Laura.shape[0]+1)],
                                    textposition='top right',
                                    name='future',
                                    marker = {
                                        'color': 'red'
                                    }
                                ),
                            ],
                            'layout':{
                                'title':'Laura Future',
                                'showlegend' : 'True',
                                'xaxis':{
                                    'title': 'Fréquence',
                                    'tickvals':[i for i in range(1,6)],
                                    'ticktext':['rare', 'peu rare', 'moyen', 'souvant', 'très souvant']
                                },
                                'hovermode':'closest',
                                'hoverlabel': {
                                    'bgcolor':'violet',
                                    'font': {
                                        'color': 'black'
                                    }
                                }
                            }})
                ], style={'width':'70%', 'display':'inline-block'}),
            ],style={'margin-left':'20%'}),
            html.Div([
                dcc.Markdown(dedent('''
                Laura a fait face aux risques concernés la machine au niveau de vol, explosition, accident au travailcar elle veux acheter le scooter et ce scooter concerne au salarité etc...
                '''))], style={'display':'inline-block', 'margin-left':'20%', 'margin-right':'20%'}
            ),
            html.H4('Risques potentiels', style={'background-color':'rgba(256,0,0,0.6)', 'text-align':'center'}),
            html.Div([
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.49,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>3</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Risques faibles</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Risques forts</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.42,
                                      "x1": 0.56,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ],style={'width':'39%', 'display':'inline-block', 'margin-top':'20px', 'margin-left':'35%'}),
            html.H4('La proposition au niveau de protection', style={'background-color':'rgba(256,0,0,0.6)', 'text-align':'center'}),
            html.Div([
                dcc.Graph(
                    figure={
                        'data':[
                            go.Scatterpolar(
                                name = "Laura actuel",
                                r = [val for key, val in data_score['Laura']['Actuel'].items()],
                                theta = [key for key, val in data_score['Laura']['Actuel'].items()],
                                fill = "toself",
                            ),
                            go.Scatterpolar(
                                name = "Laura future",
                                r = [val for key, val in data_score['Laura']['Future'].items()],
                                theta = [key for key, val in data_score['Laura']['Future'].items()],
                                fill = "toself",
                            ),
                        ],
                        'layout':{
                            'title': 'Les risques correspondent aux offres d\'assurances',
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
        
    ])

    @app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('tabs', 'value')])
    def render_content(tab):
        if tab == 'alexandre':
            return page_1_layout
        elif tab == 'laura':
            return page_2_layout
    # add js file
    external_js = ['https://code.jquery.com/jquery-3.2.1.min.js','static/js/print.js']
    for js in external_js:
        app.scripts.append_script({"external_url": js})

    return app

if __name__ == '__main__':
    app.run_server(debug=True)