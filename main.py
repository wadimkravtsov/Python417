import re
from fileinput import close

# numb=int(input('Введите пятизначное число: '))
# # numb=97531
# a=numb%10
# numb=numb//10
# b=numb%10
# numb=numb//10
# c=numb%10
# numb=numb//10
# d=numb%10
# numb=numb//10
# e=numb
# sr=(a+b+c+d+e)/5
# mult=a*b*c*d*e
# # print('Введите пятизначное число: 97531')
# print('Произведение цифр числа: ',mult)
# print('Среднее арифметическое: ',sr)

# f = open(r'C:\Dev\Python417\text.txt')
# print(f)
# print(*f)
# print(f.name)
# print(f.mode)
# print(f.encoding)
# f.close()
# print(f.closed)

#                     ЛЕКЦИЯ 15 от 26.04.2025 г.

# ==================== используем относительный путь к файлу ==============

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# ==================== запись в файл ========================================

# f = open('text1.txt', 'w')
# f.write('This is line1\nThis is line2\nThis is line3\n')
# f.close()

# ===================чтение из файла ========================================

# f = open('text1.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# ===================чтение с разбивкой строки ==============================

# f = open('text1.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# ==================== чтение списком =======================================

# f = open('text1.txt', 'r')
# print(f.readlines(10))
# print(f.readlines(5))
# f.close()

# ==================== то же, через цикл: ====================================

# f = open('text1.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# ====================== запись более подробно ===============================

# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()
#
# # ====================== дозапись в имеющийся файл ===========================
#
# f = open('xyz.txt', 'a')
# f.write('\nNew text')
# f.close()

# ===================== особенности записи файлоа =============================

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(100, 1000, 10)]
# print(lst)
# for ind in lst:
#     f.write(ind + '\t')
# f.close()

# ===================== ДЗ к занятию 16 от 27.04.2025 ==========================

#
# f = open('dz.txt', 'w') #  Запись исходного файла
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# f.close()
#
# f = open('dz.txt', 'r') #  Чтение исходного файла в список
# print('Исходный файл:' + '\n')
# print(f.read())
# f.seek(0)
# lst = (f.readlines())
# # print(lst)
# while True: #  Ввод номеров строк для обмена
#     x,y = input('Введите через запятую номера двух строк для обмена:').split(',')
#     x = int(x) - 1
#     y = int(y) - 1
#     if ((0 <= x < len(lst)) and (0 <= y < len(lst))) == False:
#         print('Неверный ввод одного из номеров, повторите.')
#     else:
#         break
#
# lst[x], lst[y] = lst[y], lst[x]
# # print(lst)
# f.close()
#
# f = open('dz.txt', 'w')  # Запись измененного файла
# for i in lst:
#     f.write(i)
# f.close()
#
# f = open('dz.txt', 'r')  # Чтение - контроль
# print('\n' + 'Конечный файл:' + '\n')
# print(f.read())

#                             ЛЕКЦИЯ 16 от 27.04.2025 г.

# Модули OS и OS.PATH:

# import os
# print(os.getcwd())
# print(os.listdir())

#                            ЛЕКЦИЯ 17 от 10.05.2025 г.

# Объектно - ориентированное программирование (ООП)


# class Point:
#     """ Класс для предоставления координат точек на плоскости"""
#
#     x = 1
#     y = 2
#
#     def set_coords(self,x1,y1):
#         self.x = x1
#         self.y = y1
#         print(self.__dict__)
#
#
# p1 = Point()
# # print(p1.x,p1.y)
#
# # p1.x = 100
# # p1.y = 200
# # print(p1.x,p1.y)
# p1.set_coords(100,200)
# Point.set_coords(p1,111,222)
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 20
# # print(p2.x,p2.y)
# p2.set_coords(10,20)
# Point.set_coords(p2,10,20)
# print(Point.__doc__)


# p2 = Point()
# print(p2.x,p2.y)
#
# print(p1.__dict__)
# print(p2.__dict__)
#
# print(Point.__dict__)
# print(Point.__doc__)
#
#
# class Human:
#
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     city = 'city'
#
#     def print_info(self):
#         print('Персональные данные'.center(40,'*'))
#         print(f"Имя: {self.name}\nДень рождения: {self.birthday}\nТелефон: {self.phone}\nГород: {self.city}")
#         print('='*40)
#
#     def input_info(self, firstday, birthday, phone, city):
#         self.name = firstday
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#
#     def set_name(self, name):  # СЕТТЕР устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # ГЕТТЕР получаем имя, которое установили в set_name
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Вадим', '24.03.1988', '63-27-93', 'Барнаул')
# h1.print_info()
# h1.set_name('Ольга Кравцова')
# h1.print_info()
# print(h1.get_name())

# ======== Инициализатор. Статические и динамические свойства. ==================

# class Point:
#     count = 0
#
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
# p1 = Point(1,2)
# p2 = Point(10,20)
# p3 = Point(100,200)
# print( Point.count)

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# Задача - РОБОТЫ!
#
# class Robot:
#     k = 0
#
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут', self.name)
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним.")
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#
#
# droid1 = Robot('R1')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid2 = Robot('R2')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid3 = Robot('R3')
# droid3.say_hi()
# print('Численность роботов:', Robot.k)
#
#
# del droid1
# del droid2
# del droid3
#
# print('Численность роботов:', Robot.k)
# print('\nЗдесь роботы могут проделать какую - то работу\n')
#
# print('Роботы выполнили работу, давйте их выключим!')

# # Модификаторы доступа:
#
# class Point:
#     """ Класс для предоставления координат точек на плоскости """
#
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check_value(c):  # Закрытый метод
#         return isinstance(c, (int,float)) # Упростили - передали в виде кортежа - либо int, либо float и всё это сразу в return
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y): # Проверка внутри класса работает
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # print((p1.__x))
# p1.set_coord(1,'2.5')
# print(p1.get_coord())

# print(Point.__dict__) # Посмотрим что теперь есть в Point?
# print(Point.__check_value(5)) # Снаружи класса обращение невозможно - ошибка!


#                            ЛЕКЦИЯ 18 от 11.05.2025 г.

# Модификаторы доступа, продолжаем в том же коде.

# class Point:
#     """ Класс для предоставления координат точек на плоскости """
#
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check_value(c):  # Закрытый метод
#         return isinstance(c, (int,float)) # Упростили - передали в виде кортежа - либо int, либо float и всё это сразу в return
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y): # Проверка внутри класса работает
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # print((p1.__x))
# # p1.set_coord(1,'2.5')
# print(p1.get_coord())
# p1._Point__x = 222  # ВСЁ РАВНО ОБОШЛИ ПРОВЕРКУ - ПРОГРАММИСТЫ ДОГОВОРИЛИСЬ ТАК НЕ ДЕЛАТЬ! Если свойство с __ то только через set, get
# print(p1.__dict__)
#
# # ещё современный вариант создания геттеров и сеттеров с декоратором:
#
# class Point:
#     """ Класс для предоставления координат точек на плоскости """
#
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#     @property  # геттер
#     def x(self):
#         print('Вызов __get_x')
#         return self.__x
#
#     @x.setter  # сеттер
#     def x(self, x):
#         print('Вызов __set_x')
#         self.__x = x
#
#     @x.deleter  # Удаление свойства
#     def x(self):
#         print('Удаление свойства')
#         del self.__x
#
# p1 = Point(5, 10)
# p1.x = 50
# print(p1.x)
# del p1.x

#  Задача - перевод килограмм в фунты
#
# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg  # _KgToPounds__kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числом')
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
# w = KgToPounds(12)
# print(w.kg, 'кг =>', w.to_pound(), 'фунтов')
# w.kg = 41
# print(w.kg, 'кг =>', w.to_pound(), 'фунтов')

# #  Закрытые статические свойства:
#
# class Point:
#     """ Класс для предоставления координат точек на плоскости """
#     __count = 0  # Закрытое статическое свойство:
#     def __init__(self,x = 0,y = 0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod  # сделали статический метод без self
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
#
#
# #                  К ЛЕКЦИИ 20 Тема: 'Абстрактные классы и методы'
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self) -> None:
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


#                    К ЛЕКЦИИ 21, ТЕМА: Вложенные классы


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def other_static_method():
#         print("Метод наружного класса")
#
#     def other_obj_method(self):
#         print("Метод экземпляра наружного класса")

    # @staticmethod
    # def other_static_method():
    #     print("Метод наружного класса")
    #
    # def other_obj_method(self):
    #     print("Метод экземпляра наружного класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj  # в инициализаторе внутреннего класс создали экземпляр наружного
#         #     self.obj = obj  # self.obj = MyOuter('внешний')
#         def inner_method(self):
#             print('метод во внутреннем классе', MyOuter.age)
#             MyOuter.other_static_method()
#         #
#         def inner_method(self):
#             print("Метод во внутреннем классе", MyOuter.age, self.obj.name)
#             MyOuter.other_static_method()
#             self.obj.other_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний',out)
# # inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# К Занятию 23 от 31.05.2025: "Модули и пакеты"

# from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())




# from autopark import *
#
# at1 = Auto1.Auto('Haval', 'Jolion', 2023, 15000)
# at1.info_auto()
# et1 = Auto2.Electric_auto('Haval', 'Jolion', 2023, 15000,95)
# et1.info_auto1()

# # К Занятию 24 от 01.06.2025 JSON - формат
#
# import json
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#     key = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'l', 'm', 'n']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     while len(key) != 10:
#         key += choice(num)
#
#     person = {
#         key:{
#         'name': name,
#         'tel': tel}
#     }
#     return person
#
# # print(gen_person())
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = {}
#
#     dict.update(data, person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# for i in range(5):
#     write_json(gen_person())

# # К занятию 25 от 07.06.2025 "JSON, CSV и тд"
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos") # Скачали файл в виде строки
# # print(type(response.text))
# todos = json.loads(response.text) # Перевели в json формат
# # print(todos)
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user) # Вывели словарь студент - количество выполненных работ
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse = True) # Отсортировали по возрастанию
# print(top_users)
#
# max_complete = top_users[0][1] # Вывели максимальное количество выполненных работ
# print(max_complete) # Это - 12
#
# users = []
# for user, num_complete in top_users: # Выводим список студентов с максимальным количеством выполненных задач
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
#
# print(f"Users {max_users} completed {max_complete} TOSos") # Печатаем номера студентов с максимальным количеством выполненных задач
#
# def keep(totdo1):
#     is_complete = totdo1["completed"]
#     has_max_count = str(totdo1["userId"]) in users
#     return is_complete and has_max_count
#
# with open("filtered_data.json", "w") as f: # Запись в файл json
#     filtered_todos = list(filter(keep, todos))
# # print (filtered_todos)
#     json.dump( filtered_todos, f, indent=2)
#
# with open("filtered_data.json", "r") as f: # Чтение из файла, проверка
#     print(json.load(f))

# CSV

import csv
from pkgutil import get_data

# with open("data.csv") as f: # Через список
#     file_reader = csv.reader(f, delimiter=";")
    # count = 0
    # for row in file_reader:
    #     if count == 0:
    #         print(f"Файл содержит столбцы: {', '.join(row)}")
    #     else:
    #         print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
    #     count += 1
    # print(f"Всего в файле {count} строки.")

# with open("data.csv") as f: # Через словарь
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1

# Записываем в CSV файл:

# import csv
#
# from urllib3.filepost import writer
#
# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=';', lineterminator="\r")
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '17'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=';', lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# ====================================== ПАРСИНГ (начало - лекция 25 от 07.06.2025) ====================================

# from bs4 import BeautifulSoup
#
# f = open("index (2).html").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[2].find("div", {"class": "name"})
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find_all("div", string="Alena") # по содержимому и
# row = soup.find("div", string="Alena").parent # его родителю
# row = soup.find("div", string="Alena").find_parent(class_="row") # по родителю с классом "row"
# row = soup.find("div", id = "whois3") # по id
# row = soup.find("div", id = "whois3").find_next_sibling() # последующий элемент того же уровня
# row = soup.find("div", id = "whois3").find_previous_sibling() # последующий элемент того же уровня
# print(row)

# # ==================================== Работа с реальным сайтом ==================================================
# import requests
# from bs4 import BeautifulSoup
#
# # r = requests.get("https://ru.wordpress.org/")
# # print(r.text)
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("h1", class_="wp-block-heading").text
#     return p1
#
# if __name__ == '__main__':
#     main()
#
# # ==================================== Работа с реальным сайтом ==================================================
# import requests
# from bs4 import BeautifulSoup
#
# # r = requests.get("https://ru.wordpress.org/")
# # print(r.text)
#
# def main():
#     url = "https://ru.wordpress.org/plugins"
#     get_data(get_html(url))
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[2]
#     plugins = p1.find_all("li")
#     for plugin in plugins:
#         name = plugin.find("h3", class_="entry-title").text
#         url = plugin.find("h3", class_="entry-title").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#         print(r)
#
#
# if __name__ == '__main__':
#     main()


# # ==================================== Работа с реальным сайтом, плагины на блоках  ===================================
# import requests
# from bs4 import BeautifulSoup
#
# # r = requests.get("https://ru.wordpress.org/")
# # print(r.text)
#
# def main():
#     url = "https://ru.wordpress.org/plugins/browse/blocks"
#     (get_data(get_html(url)))
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("li", class_="wp-block-post")
#     for el in p1:
#         name = el.find("h3", class_="entry-title").text
#         url = el.find("h3", class_="entry-title").find("a").get("href")
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         print(snippet)

#========================================== Работа с реальным сайтом через ООП ==========================================

# from laser import Parser
#
# def main():
#     for i in range(1, 5):
#         pars = Parser(f"https://www.graycell.ru/online/scanwords/{i}.html", "news.text")
#         pars.run()
#
# if __name__ == '__main__':
#     main()

# =========================================== SQLite (Занятие 28 от 15.06.2025 =========================================

import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date TEXT
#     )""")
#
#     cur.execute("DROP TABLE users")

# ================================== Занятие 29 от 21.06.2025 ==========================

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79991234567",
    # age INTEGER CHECK(age>0 AND age<100),
    # email TEXT UNIQUE
    # )""")

    # переименование таблицы
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # добавление нового столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT;
    # """)


    # переименование столбца
    # cur.execute("""
    #     ALTER TABLE person_table
    #     RENAME COLUMN address TO home_address;
    #     """)

    # # удаление таблицы
    # cur.execute("""
    #     DROP TABLE person_table;
    #       """)

    # with sqlite3.connect("db_3.db") as con:
    #     cur = con.cursor()
    #     cur.execute("""
    #         SELECT *
    #         FROM T1
    #         LIMIT 2, 5;
    #     """)
    #
    #     for res in cur:
    #         print(res)

# ===========================    Занятие 30 от 22.06.2025 "Связи между таблицами" =====================

import sqlite3


# with sqlite3.connect("person.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS companies(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL)""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     company_id INTEGER,
#     FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE SET NULL
#     )""")
#
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic  TEXT NOT NULL,
#     age INTEGER NOT NULL CHECK(age >= 17 AND age <= 50),
#     [group] TEXT NOT NULL,
#     FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        group_name TEXT NOT NULL)
#        """)
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS association(
#        lesson_id INTEGER NOT NULL,
#        group_id INTEGER NOT NULL,
#        PRIMARY KEY (lesson_id, group_id),
#        FOREIGN KEY (lesson_id) REFERENCES lessons (id),
#        FOREIGN KEY (group_id) REFERENCES groups (id)
#        )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS lessons(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT NOT NULL
#         )""")


# ========================== Занятие 32 от 29.06.2025 sql через Pycharm ==========================

# import sqlite3

# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sqlite3.connect("automobile.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

    # for car in cars_list:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)  # ('BMW', 54000),

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})

    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE 'B%';
    # UPDATE cars SET price = price + 100;
    # """)

# con = None
# try:
#     con = sqlite3.connect("automobile.db")
#     cur = con.cursor()
#     cur.executescript("""
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# with sqlite3.connect("automobile.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)

    # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    # last_id = cur.lastrowid
    # buy_id = 2
    # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_id, buy_id))

    # cur.execute("SELECT model, price FROM cars")
    # for res in cur:
    #     print(res['model'], res['price'])
    #
    # print(cur.fetchone())
    # print(cur.fetchmany(5))
#     # print(cur.fetchall())
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#     #     return False
#     # return True
#
# with sqlite3.connect("automobile.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );""")

    # img = read_ava(1)
    # if img:
    #     binary = sqlite3.Binary(img)
    #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

    # cur.execute("SELECT ava FROM users")
    # img = cur.fetchone()['ava']
    # write_ava("out.png", img)

# with sqlite3.connect("automobile.db") as con:
#     cur = con.cursor()
#     # print(con.iterdump())
#
#     for sql in con.iterdump():
#         print(sql)

# with sqlite3.connect("automobile.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)

# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ==================================== Занятия 33, 34 от 05,06 июля Запуск БД в sqlite через классы ================
#
# import os
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
# from sqlalchemy import and_, or_, not_, desc, func, distinct
#
#
# if __name__ == '__main__':
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_creator.create_database()
#
#     session = Session()
#
#     print(session.query(Lesson).all()) # вывод всей таблицы
#     print("*" * 60)
#
#     for it in session.query(Lesson): # то же столбцом
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson): # вывод одного поля таблицы (lesson_title)
#         print(it.lesson_title)
#     print("*" * 60)
#
#     print(session.query(Lesson).count()) # подсчет количества записей
#     print("*" * 60)
#
#     print(session.query(Lesson).first()) # первая запись таблицы
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(Lesson.id >= 3): # с filter - условие вывода (записи с номерами >= 3)
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('М%'))):
#         print(it)
#     print("*" * 60)
#
#     for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(association_table.c.lesson_id == Lesson.id, association_table.c.group_id == Group.id, Group.group_name == 'MDA-9'):
#         print(it, gr) # связь таблиц через промежуточную таблицу
#     print("*" * 60)
#
#     for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
#         print(it)
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title is not None).all()) # проверка на непустоту (not NULL)
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all()) # то что в списке
#     print("*" * 60)
#
#     print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all()) # не то что в списке
#     print("*" * 60)
#
#     print(session.query(Student).filter(Student.age.between(16, 17)).all()) # возраст между 16 и 17
#     print("*" * 60)
#
#     print(session.query(Student).filter(not_(Student.age.between(17, 24))).all()) # возраст 16 и 25
#     print("*" * 60)
#
#     for it in session.query(Student).filter(Student.age.like("1%")).limit(4): # первая цифра возраста - 1
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3): # то же но с 3 записи 4 позиции
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).order_by(desc(Student.surname)): # сортировка по возрастанию
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'): # Связь через JOIN студент - группа
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name): # группировка  и подсчет по названию группы
#         print(it)
#     print("*" * 60)
#
#     # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name).having(func.count(Student.surname) < 25):
#     #     print(it)
#     # print("*" * 60)
#     #
#     for it in session.query(distinct(Student.age)):
#         print(it)
#     print("*" * 60)
#
#     for it in session.query(Student.age).filter(Student.age < 20).distinct():
#         print(it)
#     print("*" * 60)

# +++++++++++++++++++++++++++++++++++++++++++++++ Запуск БД - ДЗ к занятию 34 от 06.07. +++++++++++++++++++++

# import os
#
# from aparts.database import DATABASE_NAME, Session
# import create_database_flat as db_creator
#
# if __name__ == '__main__':
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_creator.create_database()

# ============================================= Шаблонизаторы ( к занятию 33 от 05.07. ==========================

# from jinja2 import Template
#
# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)
#
#
# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)


# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
#     {% for c in cities %}
#         {% if c.id > 3 %}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == 'Москва' %}
#             <option>{{ c['city'] }}</option>
#         {% else %}
#             {{c['city']}}
#         {% endif %}
#     {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """<ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#         <li><a href='{{ i['href'] }}' class='active'>{{ i['link'] }}</a></li>
#         {% else %}
#         <li><a href='{{ i['href'] }}'>{{ i['link'] }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>"""
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)


# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44200},
#     {'model': 'Wolksvagen', 'price': 31300},
# ]
# cars = [4, 5, 6, 7, 8, 9, 10]
# tpl = "{{ cs | sum(attribute='price') }}"
# tpl = "{{ cs | sum }}"
#
# tpl = "{{ (cs | min(attribute='price')).model }}"
# tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# tpl = '''
# {% for u in users %}
# {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor %}
# '''
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)

# =============================== макроопределения ========================================

# html = """
# {% macro fun_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size={{ size }}>
# {% endmacro %}
#
# <p>{{ fun_input('username', '', 'text', 40) }}</p>
# <p>{{ fun_input('email', 'Email', 'email') }}</p>
# <p>{{ fun_input('password', 'Пароль', 'password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# # =================================================

from jinja2 import Environment, FileSystemLoader

# persons = [
#      {"name": "Алексей", "year": 18, "weight": 78.5},
#      {"name": "Никита", "year": 28, "weight": 82.3},
#      {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# html = """
# {% macro list_users(list_of_user) %}
#      <ul>
#          {% for u in list_of_user %}
#              <li>{{ u.name }} {{ caller(u) }}</li>
#          {% endfor %}
#      </ul>
#  {% endmacro %}
#
# {% call(user) list_users(users) %}
#       <ul>
#           <li>age: {{ user.year }}</li>
#           <li>weight: {{ user.weight }}</li>
#       </ul>
#   {% endcall %}
#
#
#  """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)

# ================================== ДЗ к занятию 33 от 05.07. "Шаблонизаторы' ========================

from jinja2 import Template

persons = [
     {"type": "text", "name": "firstname", "placeholder": "Имя"},
     {"type": "text", "name": "lastname", "placeholder": "Фамилия"},
     {"type": "text", "name": "address", "placeholder": "Адрес"},
     {"type": "tel", "name": "phone", "placeholder": "Телефон"},
     {"type": "email", "name": "email", "placeholder": "Почта"},

]

html = """

     {% macro fun_input(type, name, placeholder) %}                        
         <input type="{{ type }}" name="{{ name }}" placeholder = "{{placeholder}}">
     {% endmacro %}
     {% for u in users %}
     <p>{{fun_input( u.type , u.name , u.placeholder)}}</p>                                                                     
     {% endfor %}


"""

tm = Template(html)
msg = tm.render(users=persons)

print(msg)