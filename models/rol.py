from app import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    status = db.Column(db.Boolean, default = True)
    external_id = db.Column(db.String(60))
    
    
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'external_id': self.external_id,
            'status': self.status == 1 if self.status else 0
        }