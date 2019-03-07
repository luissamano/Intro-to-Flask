from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Aplicacion con Flask Python 3"


@app.route('/suma/')
@app.route('/suma/<int:uno>/<int:dos>')
def suma(uno=0, dos=0):
    suma = uno + dos
    return "suma = {}".format(suma)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
