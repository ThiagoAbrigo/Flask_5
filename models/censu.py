from app import db
import uuid

class Censu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(50))
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)
    motive = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    
    person_censu =  db.relationship('PersonCensu', backref='censu', lazy=True)
    
    @property
    def serialize(self):
        return {
            'status': self.status,
            'startdate': self.startdate,
            'enddate': self.enddate,
            'motive': self.motive,
            'external_id': self.external_id,
        }