from flask import Blueprint, jsonify, make_response, request
from controllers.motiveController import MotiveController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
api_motive = Blueprint('api_motive', __name__)

motiveC = MotiveController()

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
    },
    'required': ['name']
}

@api_motive.route('/motive', methods=["GET"])
def list():
    motives = motiveC.listMotive()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([i.serializable for i in motiveC.listMotive()])}),
        200
    )

@api_motive.route('/motive/save', methods=["POST"])
@expects_json(schema)
def saveMotive():
    data = request.json
    m = motiveC.save_str(data["name"])
    if (m >= 0):
        return make_response(
            jsonify({"msg":"OK", "code":200, "tag":[]}),
            200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data":[]}),
            400
        )


    