import collections

import flask
from flask import Flask

import constants
import my_time
from app import App
from app_config import AppConfig
from entities import QueryState
from stats import singleton

SMART_DOCTOR_TIME = 5 * 60
MIDDLE_DOCRTOR_TIME = 6 * 60
STUDENT_DOCTOR_TIME = 8 * 60

doctors = [SMART_DOCTOR_TIME, SMART_DOCTOR_TIME, SMART_DOCTOR_TIME, MIDDLE_DOCRTOR_TIME, STUDENT_DOCTOR_TIME]

config = AppConfig(max_queries=30240, sources_speed=[1 / 180, 1 / 360, 1 / 240], buffer_size=4,
                   instruments_work_time=doctors)
cmo = App(config)

server = Flask(__name__)


@server.route("/next", methods=['GET'])
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
    response["time"] = round(my_time.time, ndigits=3)
    resp = flask.make_response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@server.route("/init", methods=['GET'])
def on_load():
    init_values = {"n_sources": len(config.sources_speed), "n_buffers": config.buffer_size,
                   "n_instruments": len(config.instruments_work_time)}
    resp = flask.make_response(init_values)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@server.route("/finish")
def finish():
    cmo.run()
    singleton.stats_collector.compute_stats()
    resp = flask.make_response({"time": round(my_time.time, 3)})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@server.route("/source_table")
def source_table():
    source_table = singleton.stats_collector.source_table_dict()
    resp = flask.make_response(source_table)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@server.route("/instruments_table")
def instruments_table():
    instr_table = singleton.stats_collector.instruments_table_dict()
    resp = flask.make_response(instr_table)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


server.run()
