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

# Модификаторы доступа:

class Point:
    """ Класс для предоставления координат точек на плоскости """

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y

    def set_coord(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами')

p1 = Point(5, 10)
print(p1.__dict__)
# print((p1.__x))
p1.set_coord(1,123)
print(p1.get_coord())








