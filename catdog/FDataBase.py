import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_message(self, receiver, text):

        tm = math.floor(time.time())
        self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (receiver, text, tm))
        self.__db.commit()

        return True




    def get_posts_anonce(self):
        try:
            self.__cur.execute(f"SELECT id, receiver, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения сообщения из базы данных " + str(e))

        return []





