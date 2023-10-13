from flask import Flask, request, render_template #importando las librerias necesarias para el archivo
import cx_Oracle #para poder usar la base de datos oracle
#render_template para cargar archivos HTML

app = Flask(__name__) #CREACION DE LA APLICACION FLASK
#CONFIGURACION DE LA BASE DE DATOS ORACLE
app.config['ORACLE_DNS'] = "EJERCICIO1/EJERCICIO1@hastur:1522/XE"

# mostrar el formulario
@app.route('/')
def mostrar_formulario():  # put application's code here
    return render_template('formulario.html')
# ruta para procesar el formulario y guardar los datos en labase de datos
@app.route('/guardar',methods=['POST'])
def guardar_en_bd():
    try:
        conn = cx_Oracle.connect(app.config['ORACLE_DNS'])
        cursor = conn.cursor()

        # obtener los datos del formulario
        id_tipo_documento=request.form['id_tipo_documento']
        n_documento=request.form['n_documento']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion=request.form['direccion']
        correo=request.form['correo']
        celular=request.form['telefono']

        #inserrtar datos en la base de datos
        cursor.execute(
            "INSERT INTO PERSONA VALUES (:id_tipo_documento, :n_documento, :nombre, :apellido, :direccion, :correo, :celular)",
            id_tipo_documento=id_tipo_documento,
            n_documento=n_documento,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            correo=correo,
            celular=celular)

        conn.commit()
        cursor.close()
        conn.close()
        return 'DATOS GUARDADOS CON EXITO '
    except cx_Oracle.Error as e:
        error, = e.args
        return f"Error al guardar en la base de datos: {error.message}"


if __name__ == '__main__':
    app.run()
