from app import db
import uuid

class MotiveCensu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    
    # personcensu_id = db.Column(db.Integer, db.ForeignKey('censu_person.id'), nullable=False)
    
    # catalogue = db.relationship('Catalogue', backref='censu_person', lazy=True)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._name = value