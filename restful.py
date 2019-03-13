from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/buscar', methods=['GET'])
def buscar():
    params = request.get_json()
    if params['user'] == "admin" and params['contra'] == "123":
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
    if params['user'] == "" and params['contra'] == "":
        resp = {
            'mensaje': 'No es posible insertar'
        }
    else:
        resp = {
            'mensaje': 'Registro insertado'
        }
    return json.dumps(resp)


if __name__ == "__main__":
    app.run(debug=True)
