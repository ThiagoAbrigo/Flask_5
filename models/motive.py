from app import db
import uuid

class Motive(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    @property
    def serializable(self):
        return{
            "external_id": self.external_id,
            "name": self.name,
            "status": 1 if self.status else 0,
        }