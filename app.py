import flask
from flask import render_template
from carto_risk.dash_risk import *

server = flask.Flask(__name__)
page_carto = dash_app(server=server)

@server.route('/home')
def home():
    return render_template('homepage/home.html')

@server.route('/')
def render_dashboard():
    return page_carto

if __name__ == '__main__':
    server.run(debug=True)