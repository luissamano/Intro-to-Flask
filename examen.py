from flask import Flask, request
from flask import request
import json

app = Flask(__name__)


@app.route('/buscar', methods=['GET'])
def buscar():
    params = request.get_json()
    if params['usuario'] == "admin" and params['contra'] == "123":
        resp = {
            'estatus': True,
            'mensaje': 'Encontrado'
        }
    else:
        resp = {
            'estatus': False,
            'mensaje': 'No Encontrado'
        }
    return json.dumps(resp)


@app.route('/insertar', methods=['POST'])
def insertar():
    params = request.get_json()
    if params['usuario'] == "" and params['contra'] == "":
        resp = {
            'mensaje': 'No es posible insertar'
        }
    else:
        resp = {
            'mensaje': 'Registro insertado'
        }
    return json.dumps(resp)


@app.route('/modificar', methods=['PUT'])
def modificar():
    params = request.get_json()
    if params['usuario'] == "" or params['contra'] == "":
        response = {
            'mensaje': 'No se modifico'
        }
    else:
        response = {
            'mensaje': 'Se modifico'
        }
    return json.dumps(response)


@app.route('/actualizar', methods=['PATCH'])
def actualizar():
    params = request.get_json()

    # Si alguno de los cqampos esta vacio envia el error
    if params['usuario'] == "" or params['contra'] == "":
        response = {
            'mensaje': 'No se actualizo'
        }
    else:  # Si los dos campos tienen minimo un caractert manda el mesaje de aceptacion
        response = {
            'mensaje': 'Se actualizo'
        }
    return json.dumps(response)


@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    params = request.get_json()

    # Si alguno de los cqampos esta vacio envia el error
    if params['usuario'] == "" or params['contra'] == "":
        response = {
            'mensaje': 'No se elimino'
        }
    else:  # Si los dos campos tienen minimo un caractert manda el mesaje de aceptacion
        response = {
            'mensaje': 'Se elimino'
        }
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)
