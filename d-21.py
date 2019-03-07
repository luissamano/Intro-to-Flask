from flask import Flask
from flask import render_template

app=Flask(__name__, )

@app.errorhandler(404)
def pagina_no_encontrada():
    return render_template('404.html')


@app.route('/')
def index():
    return "flask python"

@app.route('/suma/')
@app.route('/suma/<float:uno>/')
@app.route('/suma/<float:uno>/<floatdos>/')
def suma(uno=0,dos=0):
    suma = uno + dos
    return "suma = {}".format(suma)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
