from flask import Flask, request
from flask import request
import json

app = Flask(__name__)


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
