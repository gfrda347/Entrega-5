from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aquí se renderiza el archivo de plantilla 'index.html'
    return render_template('index.html')
