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


f = open('dz.txt', 'w') #  Запись исходного файла
f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
f.close()

f = open('dz.txt', 'r') #  Чтение исходного файла в список
print('Исходный файл:' + '\n')
print(f.read())
f.seek(0)
lst = (f.readlines())
# print(lst)
while True: #  Ввод номеров строк для обмена
    x,y = input('Введите через запятую номера двух строк для обмена:').split(',')
    x = int(x) - 1
    y = int(y) - 1
    if ((0 <= x < len(lst)) and (0 <= y < len(lst))) == False:
        print('Неверный ввод одного из номеров, повторите.')
    else:
        break

lst[x], lst[y] = lst[y], lst[x]
# print(lst)
f.close()

f = open('dz.txt', 'w')  # Запись измененного файла
for i in lst:
    f.write(i)
f.close()

f = open('dz.txt', 'r')  # Чтение - контроль
print('\n' + 'Конечный файл:' + '\n')
print(f.read())



