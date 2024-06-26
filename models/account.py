from app import db
import uuid
from datetime import datetime
class Account(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(10), default='activo')
    password = db.Column(db.String(250))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False, unique=True)
    
    # def copy(self, value):
    
    @property
    def serialize(self):
        return {
            'email': self.email,
            'status': 1 if self.status else 0,
            'external_id': self.external_id,
        } 
        
    def getPerson(self, id_p):
        print("Recibir: ", id_p)
        from models.person import Person
        return Person.query.filter_by(id=id_p).first()
    
    def copy(self, value):
        self.email = value.email
        self.status = value.status
        self.password = value.password
        self.id = value.id
        self.external_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return self