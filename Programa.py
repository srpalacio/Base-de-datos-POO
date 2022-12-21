from flask import Flask , render_template, request, redirect, url_for
from db import db
from Apartamento import Apartamento

class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///apartamentos.sqlite3"
        
        db.init_app(self.app)
        
        self.app.add_url_rule('/',view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo',view_func=self.agregar, methods=["GET","POST"])
        
        with self.app.app_context():
            db.create_all()
        
        self.app.run(debug=True)
        
    def buscarTodos(self):
        
        return render_template('mostrarTodos.html', apartamentos=Apartamento.query.all()) 
        
    def agregar(self):
        
        if request.method=="POST":
            direccion=request.form['direccion']
            area=request.form['area']
            edad=request.form['edad']
            parqueaderos=request.form['parqueaderos']
            valor=request.form['valor']
            telefono=request.form['telefono']
            propietario=request.form['propietario']
            observaciones=request.form['observaciones']
            
            miApartamento=Apartamento(direccion,area,edad,parqueaderos,valor,telefono,propietario,observaciones)
            
            db.session.add(miApartamento)
            db.session.commit()
            
            return redirect(url_for('buscarTodos'))
            
        
        return render_template('nuevoApartamento.html')
    
miPrograma=Programa()