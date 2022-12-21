from flask import Flask , render_template
from db import db

class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///apartamentos.sqlite3"
        
        self.app.add_url_rule('/nuevo',view_func=self.agregar)
        
        with self.app.app_context():
            db.create_all()
        
        self.app.run(debug=True)
        
    def agregar(self):
        
        return render_template('nuevoApartamento.html')
    
miPrograma=Programa()