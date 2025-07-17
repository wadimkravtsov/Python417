from flask import Flask, render_template, request,flash,g
import os
import sqlite3
from fdatabase import FDataBase

app = Flask(__name__)
DATABASE = 'flsk_new.db'
DEBUG = True
SECRET_KEY = '618a561af4167033f88abce282adbaa211f19069'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'flsk_new.db'))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db_new.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())

@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_post.html', title="Добавление статьи", menu=dbase.get_menu())

@app.route("/add_par", methods=["POST", "GET"])
def add_par():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_par.html', title="Добавление параграфа", menu=dbase.get_menu())

@app.route("/add_autor", methods=["POST", "GET"])
def add_autor():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_autor.html', title="АВТОРА!", menu=dbase.get_menu())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=[])

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == '__main__':
    app.run()