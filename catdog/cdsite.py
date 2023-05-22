from flask import Flask, render_template, url_for, request, flash, session, redirect, g, abort
import os
import sqlite3
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'gffdlkgjfgroiejlkfgdn34985kjfg'

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'catdog.db')))


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


menu = [
    {"name": "Котопес", "url": "index"},
    {"name": "Кот", "url": "cat"},
    {"name": "Пес", "url": "dog"},
    {"name": "Написать сообщение", "url": "message"},
]

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/index")
@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title="Котопес", menu=menu, posts=dbase.get_posts_anonce())



@app.route("/cat")
def cat():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('cat.html', title="Кот", menu=menu, posts=dbase.get_posts_anonce())

@app.route("/dog")
def dog():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('dog.html', title="Пес", menu=menu, posts=dbase.get_posts_anonce())

@app.route("/message", methods=["POST", "GET"])
def message():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['name']) > 2 and len(request.form['post']) > 3:
            res = dbase.add_message(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка отправки сообщения', category='error')
            else:
                flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки сообщения', category='error')
    return render_template('message.html', title="Добавление сообщения", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
