from flask import Flask, render_template
from sql import Sql

from simulator import main

db = Sql()
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/trains')
def trains():
    return render_template('trains.html', trains=db.trains, train_templates = db.train_templ)

@app.route('/terminals')
def terminals():
    return render_template('terminals.html', terminals = db.terminals, terminal_templates = db.term_templ)

@app.route('/paths')
def pathsPage():
    return render_template('paths.html', paths = db.paths)

@app.route('/calc')
def calc():
    main()
    return render_template('calc.html', paths = db.paths)

def main():
    app.run(debug=True, host = '127.0.0.1')