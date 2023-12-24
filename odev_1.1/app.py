from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hakkinda/')
def hakkinda():
    return render_template('hakkinda.html')

@app.route('/projeler/')
def projeler():
    return render_template('projeler.html')

@app.route('/iletisim/')
def iletisim():
    return render_template('iletisim.html')

@app.route('/fotograf/')
def fotograf():
    return render_template('fotograf.html')

if __name__ == '__main__':
    app.run(debug=True)
