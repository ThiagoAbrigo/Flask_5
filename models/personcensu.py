from app import db
import uuid

class PersonCensu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    motive = db.Column(db.String(50))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    censu_id =  db.Column(db.Integer, db.ForeignKey('censu.id'), nullable=False)
    #person_id =  db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    #motive_censu = db.relationship('MotiveCensu', backref='censu_person', lazy=True)