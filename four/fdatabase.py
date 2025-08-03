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

    def add_course(self, title, text, price):
        try:
            # tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO courses VALUES(NULL, ?, ?, ?)", (title, text, price))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД " + str(e))
            return False

    def get_course(self, course_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM courses WHERE id = '{course_id}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))

        return False, False

    def get_courses_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, price FROM courses")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))

        return []