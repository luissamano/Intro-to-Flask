from flask import Flask, render_template

app = Flask(__name__)


@app.route('/avisos')
@app.route('/avisos/<mensage>')
def avisos(mensage=''):
    return render_template('avisos.html', msg=mensage)


if __name__ == "__main__":
    app.run(debug=1, port=8000)
