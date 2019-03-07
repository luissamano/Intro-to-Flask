from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Aplicación web en Flask Python 3"


@app.route('/')
@app.route('/get/<uno>/')
@app.route('/get/<uno>/<dos>')
def get(uno='Valor por defecto', dos="0"):
    return "Parametro = {}, {}".format(uno, dos)


if __name__ == "__main__":
    app.run(port=8000)
