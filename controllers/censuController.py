# from models.censu import Censu
# from app import db
# import uuid

# class CensuController:
#     def listCensu(self):
#         return Censu.query.all()
    
#     def save_censu(self, data):
#         censu = Censu()
#         censu.status = data["status"]
#         censu.startdate = data["startdate"]
#         censu.enddate = data["enddate"]
#         censu.motive = data["motive"]
#         censu.external_id = uuid.uuid4()
                
#         db.session.add(censu)
#         db.session.commit()
                
#         return censu
    
#     def search_external(self, external):
#         censu = Censu.query.filter_by(external_id=external).first()
#         if censu:
#             return censu
#         else:
#             return None
        
#     def modify_censu(self, data):
#         censu = Censu.query.filter_by(external_id=data["external_id"]).first()
#         if censu:
#             if "status" in data:
#                 censu.status = data["status"]
#             if "startdate" in data:
#                 censu.startdate = data["startdate"]
#             if "enddate" in data:
#                 censu.enddate = data["enddate"]
#             if "motive" in data:
#                 censu.motive = data["motive"]
                
#             new_external_id = str(uuid.uuid4())
#             censu.external_id = new_external_id
#             db.session.commit()
#             modified_censu = Censu(
#                 status=censu.status,
#                 startdate=censu.startdate,
#                 enddate=censu.enddate,
#                 motive=censu.motive,
#                 external_id=new_external_id
#             )
#             return modified_censu
#         else:
#             return -3