from flask import Blueprint, jsonify, make_response, request
from controllers.personController import PersonController
from controllers.utilities.errors import Errors
from flask_expects_json import expects_json
api_person = Blueprint('api_person', __name__)

personC = PersonController()

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
schema_censador = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'lastname': {'type': 'string'},
        'age': {'type': 'string'},
        'status': {'type': 'string'},
        'email': {'type': 'string',
                   "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
        'password': {'type': 'string'},
    },
    'required': ['name', 'lastname', 'age', 'status', 'email', 'password']
}

#API for person
@api_person.route('/person', methods=["GET"])
def list():
    persons = personC.listPerson()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([person.serialize() for person in persons])}),
        200
    )
    
@api_person.route('/person/<external>', methods=["GET"])
def search_external(external):
    search = personC.search_external(external)
    if search is None:
        return make_response(
            jsonify({"msg": "Person not found", "code": "404"}), 
            404
            )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": "200", "data": search.serialize}), 
            200
            )
    
# @api_person.route('/person/save/censado', methods=["POST"])
# @expects_json(schema)
# def create():
#     data = request.json
#     person_id = personC.save_censado(data)
#     if(person_id >= 0):
#         return make_response(
#             jsonify({"msg":"OK", "code":200, "data": []}),
#             200
#         )
#     else:
#         return make_response(
#             jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.passwordrepeat[str(person_id)]}}),
#             400
#         )
#para modificar debo enviar el external, pero primero obtener el objeto, creaer metodo listar q=pero que retorne el objeto con el external id
@api_person.route('/person/save/censador', methods=["POST"])
@expects_json(schema_censador)
def create():
    data = request.json
    person_id = personC.save_censador(data)
    if(person_id >= 0):
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"tag":"saved data"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.error["-1"]}}),
            400
        )
@api_person.route('/modify_person', methods=['POST'])
def modify_person():
    data = request.json
    modified_person = personC.modify_person(data)
    if (modified_person == -3):
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': Errors.person_not_found["-3"]}), 400
        ) 
    else:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"person_saved":"saved data"}}),200
        )

@api_person.route('/deactivate_person/<external_id>', methods=['GET'])
def delete_person(external_id):
    success = personC.desactivate_account(external_id)
    if success:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"account":"Deactivated account"}}),200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': 'The person with the external_id does not exist'}), 404
        ) 
            
        