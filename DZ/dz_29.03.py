a = "Python"
b = "Programming language"
print('Буквы которые есть в первой строке, но отсутствуют во второй:', end = ' ')
for i in set(a) - set(b):
    print(i, end = ' ')