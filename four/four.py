from django.template.defaultfilters import title
from flask import Flask, render_template, request,flash, g, abort
import os
import sqlite3
from fdatabase import FDataBase

DATABASE = 'four.db'
DEBUG = True
SECRET_KEY = "ba42315d772179830632cf84b2ce89682fed125c"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'four.db'))

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
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
    return render_template('index.html', menu=dbase.get_menu(), title="Курсы по программированию", courses=dbase.get_courses_annonce())

@app.route("/add_course", methods=["POST", "GET"])
def add_course():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['course']) > 10:
            res = dbase.add_course(request.form['name'], request.form['course'], request.form['price'])
            if not res:
                flash("Ошибка добавления курса", category="error")
            else:
                flash("Курс добавлен успешно", category="success")
        else:
            flash("Ошибка добавления курса", category="error")

    return render_template('add_course.html', title="Добавление курса", menu=dbase.get_menu())

@app.route("/course/<int:id_course>")
def show_post(id_course):
    db = get_db()
    dbase = FDataBase(db)
    title, course = dbase.get_course(id_course)
    if not title:
        abort(404)
    return render_template('course.html', menu=dbase.get_menu(), title=title, course=course)

@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == '__main__':
    app.run()