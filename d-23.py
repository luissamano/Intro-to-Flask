from flask import Flask, render_template

app = Flask(__name__)


@app.route('/avisos')
@app.route('/avisos/<mensage>')
def avisos(mensage=''):
    anio = 2018
    nombres = ['hugo', 'paco', 'luis']
    return render_template('avisos1.html', msg=mensage, anio=anio, nombres=nombres)


if __name__ == "__main__":
    app.run(debug=1, port=8000)
