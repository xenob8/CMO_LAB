import flask

import constants
import main
from flask import Flask

app = Flask(__name__)

@app.route("/next", methods=['GET'])
def hello_world():
    # resp = main.update()
    resp = flask.make_response(main.update())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/init", methods=['GET'])
def on_load():
    init_values = {"n_sources": constants.N_SOURCES, "n_buffers": constants.N_BUFFERS, "n_instruments": constants.N_INSTUMENTS}
    resp = flask.make_response(init_values)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run()