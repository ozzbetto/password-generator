from flask import Flask, render_template, request
from password_generator import generate_password # Asegurar de que el script de generación de contraseñas esté en el mismo directorio con el nombre 'password_generator.py'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()
