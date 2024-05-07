from app import db
import uuid

class PersonCensu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    motive = db.Column(db.String(250))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    id_person =  db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    id_censu =  db.Column(db.Integer, db.ForeignKey('censu.id'), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
