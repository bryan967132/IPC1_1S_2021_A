#Importaciones de Flask

from flask import Flask,request,jsonify
from flask_cors import CORS
from Gestor import Gestor

#Crear la app

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

gestor = Gestor()

#EndPoints

@app.route('/',methods=['GET'])
def home():
    return 'SERVER IS WORKING!!!'

@app.route('/obtenerlibros')
def obtenerlibros():
    return gestor.obtener_libros()

@app.route('/obtenerusuarios')
def obtenerusuarios():
    return gestor.obtener_usuarios()

@app.route('/libros',methods=['POST'])
def crearlibro():
    dato = request.json
    gestor.crearLibro(dato['titulo'],dato['autor'],dato['imagen'],dato['descripcion'])
    return '{"Estado":"Libro Creado"}'

@app.route('/libros/<titulo>/<autor>',methods=['DELETE'])
def eliminarlibro(titulo,autor):
    if(gestor.eliminar_libro(titulo,autor)):
        return '{"data":"Eliminado"}'
    return '{"data":"Error"}'

@app.route('/libros/<titulo>',methods=['PUT'])
def actualizarlibro(titulo):
    dato = request.json
    if(gestor.actualizar_libro(titulo,dato['titulo'],dato['autor'],dato['imagen'],dato['descripcion'])):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'

@app.route('/buscarlibros/<titulo>',methods=['GET'])
def buscarlibro1(titulo):
    if(gestor.buscar_libro(titulo)):
        return gestor.buscar_libro(titulo)
    return '{"data":"Error"}'

@app.route('/buscarlibros',methods=['GET'])
def buscarlibros2():
    dato = request.json
    if gestor.buscar_libro(dato['titulo']):
        return gestor.buscar_libro(dato['titulo'])
    return '{"data":"Inexistente"}'

@app.route('/login/<usuario>/<password>')
def login(usuario,password):
    return gestor.iniciar_sesion(usuario,password)

@app.route('/registro',methods=['POST'])
def registrar():
    dato = request.json
    gestor.registrar_usuario(dato['nombre'],dato['apellido'],dato['password'],dato['usuario'])
    return '{"data":"Creado"}'

#Iniciar el Servidor

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)