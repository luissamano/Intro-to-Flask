from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Aplicacion con Flask Python 3"


@app.route('/get')
@app.route('/get/<uno>/')
def get(uno='valor por defecto'):
    return "Parametro = {}".format(uno)


if __name__ == "__main__":
    app.run(degub=1, port=8000)
