from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import os
import sqlite3

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'gffdlkgjfgroiejlkfgdn34985kjfg'

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'gffdlkgjfgroiejlkfgdn34985kjfg'
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

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
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
]

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/index")
@app.route("/")
def index():
    db = get_db()
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('cat.html', title="О нас", menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Данные отправлены', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('dog.html', title="Обратная связь", menu=menu, **context)
    return render_template('dog.html', title="Обратная связь", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'marina'and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()



if __name__ == '__main__':
    app.run(debug=True)
