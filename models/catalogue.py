from app import db
import uuid

class Catalogue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    #external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    
    #motive_censu_id = db.Column(db.Integer, db.ForeignKey('motive_censu.id'), nullable=False)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._name = value

    @property
    def external_id(self):
        return self._external_id
    
    @external_id.setter
    def external_id(self, value):
        if not value:
            raise ValueError("El external_id no puede estar vacío")
        self._external_id = value
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if not value:
            raise ValueError("El status no puede estar vacío")
        self.status = value

