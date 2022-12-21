from db import db

class Apartamento(db.Model):
    
    __tablename__="apartamento"
    
    id=db.Column(db.Integer,primary_key=True)
    
    direccion=db.Column(db.String(100))
    area=db.Column(db.String(10))
    edad=db.Column(db.String(10))
    parqueaderos=db.Column(db.String(10))
    valor=db.Column(db.String(70))
    telefono=db.Column(db.String(15))
    propietario=db.Column(db.String(70))
    observaciones=db.Column(db.String(500))
    
    def __init__(self,direccion,area,edad,parqueaderos,valor,telefono,propietario,observaciones):
        
        self.direccion=direccion
        self.area=area
        self.edad=edad
        self.parqueaderos=parqueaderos
        self.valor=valor
        self.telefono=telefono
        self.propietario=propietario
        self.observaciones=observaciones
    
    