from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Aplicación web en Flask Python 3"


@app.route('/get/<uno>')
def index(uno):
    return "Parametro = {}".format(uno)


if __name__ == "__main__":
    app.run(degub=1, port=8000)
