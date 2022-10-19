import collections

import flask

import constants
from flask import Flask

import my_time
from app import App
from entities import QueryState

cmo = App(100)

app = Flask(__name__)

@app.route("/next", methods=['GET'])
def hello_world():
    cmo.update()
    response = collections.defaultdict(dict)
    if cmo.last_source_query.state == QueryState.FROM_SOURCE:
        response["inputs"]["n_source"] = cmo.last_source_query.n_source
        response["inputs"]["n_query"] = cmo.last_source_query.n_query
    else:
        response["inputs"] = None
    response["buffers"] = [q.point_to_str() for q in cmo.put_disp.buffers]
    response["instruments"] = [instr.query.point_to_str() if instr.is_busy else '-' for instr in cmo.instruments]
    response["cancel"] = cmo.put_disp.refused_query.point_to_str() if cmo.put_disp.refused_query else "-"
    response["time"] = round(my_time.time,ndigits=3)
    resp = flask.make_response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/init", methods=['GET'])
def on_load():
    init_values = {"n_sources": constants.N_SOURCES, "n_buffers": constants.N_BUFFERS, "n_instruments": constants.N_INSTUMENTS}
    resp = flask.make_response(init_values)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run()