from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db
import uuid
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app

class PersonController:
    def listPerson(self):
        return Person.query.all()
    
    # def save_censado(self,data):
    #     rol = Rol.query.filter_by(nombre="CENSADO").first()
    #     persona = Person()
    #     if rol:
    #         persona.external_id = uuid.uuid4()
    #         persona.apellido = data.get("apellido")
    #         persona.nombre = data.get("nombre")
    #         persona.estado_civil = data.get("estado_civil")
    #         persona.rol_id = rol.id
    #         db.session.add(persona)
    #         db.session.commit()
    #         return  persona.id
    #     else:
    #         return -1
        
    def save_censador(self, data):
        person = Person()
        rol = Rol.query.filter_by(name='Admin').first()
        if rol:
            accounts = Account.query.filter_by(email = data["email"]).first()
            if accounts:
                return -2
            else:
                person.name = data["name"]
                person.lastname = data["lastname"]
                person.age = data["age"]
                person.external_id = uuid.uuid4()
                person.civilstatus = data["status"]
                #verificar aqui
                person.rol_id = rol.id
                db.session.add(person)
                db.session.commit()
                #account
                account = Account()
                account.email = data["email"] 
                account.password = data["password"]  
                account.external_id = uuid.uuid4()
                account.person_id = person.id
                db.session.add(account)
                db.session.commit()
                return account.id
        else:
            return -1
    def search_external(self, external):
        person = Person.query.filter_by(external_id=external).first()
        if person:
            return person
        else:
            return None
        
    def modify_person(self, data):
        person = Person.query.filter_by(external_id=data["external_id"]).first() #sql 
        if person:
            if "name" in data:
                person.name = data["name"]
            if "lastname" in data:
                person.lastname = data["lastname"]
            if "age" in data:
                person.age = data["age"]
                
            new_external_id = str(uuid.uuid4())
            person.external_id = new_external_id
            db.session.commit()
            modified_person = Person(
                name=person.name,
                lastname=person.lastname,
                age=person.age,
                external_id=new_external_id
            )
            return modified_person
        else:
            return -3
        
    def desactivate_account(self, external_id):
        person = Person.query.filter_by(external_id=external_id).first()
        if person:
            for account in person.account:
                account.status = 'desactivo' 
            db.session.commit()
            return True
        else:
            return False
    
    #use AccountController
    def login(self, data):
        accountA = Account.query.filter_by(email=data["email"]).first()
        if accountA:
            #decrypt password
            if accountA.password == data["password"]:
                token_payload = {
                    "external_id": accountA.external_id,
                    "expire": (datetime.now(timezone.utc) + timedelta(minutes=60)).isoformat()
                }
                print('-------------', token_payload)
                token = jwt.encode(
                    token_payload,
                    key=current_app.config["SECRET_KEY"],
                    algorithm="HS512"
                )
                account = Account()
                account.copy(accountA)    
                person = accountA.getPerson(accountA.person_id)
                user_info = {
                    "token": token,
                    "user": person.lastname + " " + person.name
                }
                return user_info
            else:
                -6
        else:
            return -6