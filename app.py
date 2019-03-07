from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask!"


@app.route('/acceso')
def acceso():
    return "Sesion"


"""
@app.route('/get')
def get():
    param = request.args.get('valor': 'vacio')
    p2 = request.args.get('dos': 'vacio')
    return "Parametro = {}, {}".format(param, p2)
"""


@app.route('/suma', methods=['GET'])
def suma():

    # Se recuperan los parametros de la peticion
    n1 = request.args.get('num', default=None, type=int)
    n2 = request.args.get('nums', default=None, type=int)

    # Se realiza la operacion
    suma = n1 + n2

    # Regresa el valor resultado de la suma
    return "La suma de los dos numeros es = {}".format(suma)


#if __name__ == "__main__":
#    app.run(debug=True, port=8000)
