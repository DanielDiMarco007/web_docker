from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="servidor-bd",
        user="root",
        password="123456",
        database="adso_db"
    )

@app.route('/')
def index():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM aprendices")
    aprendices = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("index.html", aprendices=aprendices)

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    documento = request.form['documento']
    ficha = request.form['ficha']

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO aprendices
        (nombre_completo, numero_documento, ficha)
        VALUES (%s, %s, %s)
        """,
        (nombre, documento, ficha)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
