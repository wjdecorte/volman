import logging

from flask import jsonify, request
from flask_smorest import Blueprint

from connectors import __version__, get_config
from connectors.routes.api_connectors import APIConnectorRoot
from connectors.routes.file_connectors import FileConnectorRoot

logger = logging.getLogger(__name__)

config = get_config()

api = Blueprint(name="Common", import_name=__name__, description="Common Endpoints")


@api.route("/version", methods=["GET"])
def get_info():
    response = dict(
        version=__version__,
        config=config.__dict__,
    )
    return jsonify(response)


@api.route("/healthcheck", methods=["GET"])
def get_healthcheck():
    return jsonify({"msg": "Happy"})


@api.route("/all")
def get_all_connectors():
    logger.info("Get all Connectors")
    fc = FileConnectorRoot().get()
    ac = APIConnectorRoot().get()
    return jsonify(dict(connectors=dict(fileConnectors=fc.json, apiConnectors=ac.json)))


@api.route("/repeat", methods=["POST"])
def repeater():
    logger.info("test route")
    body = request.get_json(silent=True)
    return jsonify(body)
