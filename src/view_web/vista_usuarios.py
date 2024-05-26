from flask import Flask, render_template, request, redirect, url_for, flash
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '../../templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'  

# Conexión a la base de datos
def conectar_db():
    # Aquí iría la conexión a la base de datos
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_usuario = request.form['id_usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        documento_identidad = request.form['documento_identidad']
        correo_electronico = request.form['correo_electronico']
        telefono = request.form['telefono']
        salario = request.form['salario']
        
        # Conectar a la base de datos y agregar usuario
        
        flash('Usuario agregado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('agregar_usuario.html')

@app.route('/agregar_declaracion', methods=['GET', 'POST'])
def agregar_declaracion():
    # Lógica para manejar la adición de declaraciones
    return render_template('agregar_declaracion.html')

@app.route('/consultar_usuario', methods=['GET', 'POST'])
def consultar_usuario():
    usuario = None
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        
        # Conectar a la base de datos y consultar usuario
        # Aquí iría la lógica para consultar los datos del usuario en la base de datos
        
        # Suponiendo que el resultado de la consulta se almacene en la variable usuario
    
    return render_template('consultar_usuario.html', usuario=usuario)

@app.route('/eliminar_usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        
        # Conectar a la base de datos y eliminar usuario
        # Aquí iría la lógica para eliminar el usuario de la base de datos
        
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('eliminar_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)
