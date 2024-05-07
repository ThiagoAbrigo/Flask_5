from app import db
import uuid

class Censu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.Boolean, default=True)
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)
    motive = db.Column(db.String(50))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    @property
    def serialize(self):
        return {
            "status": 1 if self.status else 0,
            'startdate': self.startdate,
            'enddate': self.enddate,
            'motive': self.motive,
            'external_id': self.external_id,
        }