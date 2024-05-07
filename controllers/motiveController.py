from models.motive import Motive
from app import db
from tokenizer import split_into_sentences
import uuid

class MotiveController:
    def listMotive(self):
        return Motive.query.all()
    
    def save_str(self, text):
        g = split_into_sentences(text)
        tokens = []
        for sentence in g:
            tokens = sentence.split()
            print (tokens)
        
        #save
        if len(tokens) > 0:
            for m in tokens:
                motive = Motive()
                motive.name = m
                motive.status = True
                motive.external_id = uuid.uuid4()
                db.session.add(motive)
                db.session.commit()
                return 0
            else:
                return -3
            
    #motivos que estes en verdadero debes mostrarse
    # def list_activate(self):
    #     return 