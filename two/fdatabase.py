import math
import time
import sqlite3
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

    def add_post(self, title, text, url):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False

    def get_post(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE url = '{alias}'")
            res = self.__cur.fetchone()
            if res:
                 return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return False, False

    def get_posts_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []
