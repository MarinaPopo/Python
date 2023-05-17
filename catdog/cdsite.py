from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import os
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ghffdlkgjfgroiejlkfgdn34985kjfg'
app.config.from_object(__name__)


menu = [
    {"name": "Котопес", "url": "index"},
    {"name": "Кот", "url": "cat"},
    {"name": "Пес", "url": "dog"},
]

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title="Котопес", menu=menu)


@app.route("/cat")
def cat():
    return render_template('cat.html', title="Кот", menu=menu)

@app.route("/dog")
def dog():
    return render_template('dog.html', title="Пес", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
