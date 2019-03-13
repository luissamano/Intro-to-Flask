from flask import Flask, request
import json

app = Flask(__name__)


""" JSON CORRECTO A ENVIAR
{
	"usuario": "a",
	"contra": "b"
}
"""

""" JSON INCORRECTO A ENVIAR
{
	"usuario": "",
	"contra": "b"
}
"""


@app.route('/modificar', methods=['PUT'])
def modificar():
    params = request.get_json()

    if params['usuario'] == "" or params['contra'] == "": #Si alguno de los cqampos esta vacio envia el error
        response = {
            'mensaje': 'No se modifico'
        }
    else:                                                 #Si los dos campos tienen minimo un caractert manda el mesaje de aceptacion
        response = {
            'mensaje': 'Se modifico'
        }
    return json.dumps(response)


@app.route('/actualizar', methods=['PATCH'])
def actualizar():
    params = request.get_json()

    if params['usuario'] == "" or params['contra'] == "": #Si alguno de los cqampos esta vacio envia el error
        response = {
            'mensaje': 'No se actualizo'
        }
    else:                                                 #Si los dos campos tienen minimo un caractert manda el mesaje de aceptacion
        response = {
            'mensaje': 'Se actualizo'
        }
    return json.dumps(response)


@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    params = request.get_json()

    if params['usuario'] == "" or params['contra'] == "": #Si alguno de los cqampos esta vacio envia el error
        response = {
            'mensaje': 'No se elimino'
        }
    else:                                                 #Si los dos campos tienen minimo un caractert manda el mesaje de aceptacion
        response = {
            'mensaje': 'Se elimino'
        }
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)