from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    edad = db.Column(db.Integer)
    dni = db.Column(db.Integer)
    habitacion = db.Column(db.Integer)
    diagnostico = db.Column(db.String(200))
    
    def __init__(self, nombre, edad, dni, habitacion, diagnostico):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.habitacion = habitacion
        self.diagnostico = diagnostico
    
    def __str__(self):
        return "\nnombre {} edad {} dni {} habitacion {} diagnostico {}.\n".format(self.nombre, self.edad, self.dni, self.habitacion, self.diagnostico)
    
    def convert(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "dni": self.dni,
            "habitacion": self.habitacion,
            "diagnostico": self.diagnostico
        }
    

