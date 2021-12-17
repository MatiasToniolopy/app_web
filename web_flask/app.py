
from flask import Flask, request, render_template, redirect, url_for, flash
import traceback
from models import db, Persona
import sqlite3 as sql





app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
db.init_app(app)

app.secret_key = 'mysecretkey'

@app.route('/')

def index():
    conn = sql.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paciente')
    data = cursor.fetchall()
    return render_template('index.html', pacientes=data)


@app.route('/agregarpaciente', methods=['POST'])

def agregarpaciente():
    if request.method == 'POST':
        try:
            
           nombre = request.form['nombre']
           edad = request.form['edad']
           dni = request.form['dni']
           habitacion = request.form['habitacion']
           diagnostico = request.form['diagnostico']
        
           nuevo_paciente = Persona(nombre, int(edad), int(dni), int(habitacion), diagnostico)
           db.session.add(nuevo_paciente)
           db.session.commit()
           flash('Paciente agregado satisfactoriamente')
           return redirect(url_for('index'))
           #return jsonify (nuevo_paciente.convert())
        except:
            return({'trace': traceback.format_exc()})
        
        
        
@app.route('/editar/<id>', methods=['GET', 'POST'])

def editar(id):
    
    conn = sql.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paciente WHERE id = ?;', (id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('editar.html', paciente=data[0])

@app.route('/actualizar/<id>', methods=['POST'])

def actualizar(id):
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        dni = request.form['dni']
        habitacion = request.form['habitacion']
        diagnostico = request.form['diagnostico']
        
        conn = sql.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE paciente SET nombre = ?, edad = ?, dni = ?, habitacion = ?, diagnostico = ? WHERE id = ?', (nombre, edad, dni, habitacion, diagnostico, id))
        conn.commit()
        flash('Paciente actualizado correctamente')
        return redirect(url_for('index'))
        
                   


@app.route('/eliminar/<string:id>')

def eliminar(id):
    
    conn = sql.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM paciente WHERE id = {0}'.format(id))
    conn.commit()
    flash('Paciente eliminado correctamente')
    return redirect(url_for('index'))

















if __name__ == '__main__':
    app.run(debug=True, port=4000)
