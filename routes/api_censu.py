from flask import Blueprint, jsonify, make_response, request
from controllers.censuController import CensuController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
api_censu = Blueprint('api_censu', __name__)

censuC = CensuController()

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'lastname': {'type': 'string'},
        'age': {'type': 'string'},
        'status': {'type': 'string'},
        'rol_id': {'type': 'integer'},
    },
    'required': ['name', 'lastname', 'age', 'status']
}

#API for censu
@api_censu.route('/censu', methods=["GET"])
def list():
    census = censuC.listCensu()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([censu.serialize() for censu in census])}),
        200
    )
    
@api_censu.route('/censu/<external>')
def search_external(external):
    search = censuC.search_external(external)
    if search is None:
        return make_response(
            jsonify({"msg": "Censu not found", "code": "404"}), 
            404
            )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": "200", "data": search.serialize}), 
            200
            )
    
@api_censu.route('/censu/save', methods=["POST"])
# @expects_json(schema)
def create():
    data = request.json
    censu = censuC.save_censu(data)

    if censu:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"tag":"saved data"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.error[str(censu)]}}),
            400
        )
@api_censu.route('/modify_censu', methods=['POST'])
def modify_person():
    data = request.json
    modified_censu = censuC.modify_censu(data)
    if (modified_censu == -3):
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': Errors.person_not_found["-3"]}), 400
        ) 
    else:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"censu_saved":"saved data"}}),200
        )

            
        