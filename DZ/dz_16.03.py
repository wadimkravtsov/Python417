import random
a = [random.randint(-9,9) for i in range(int(input('Введите n: ')))]
print('Исходный список: ',a)
b=[]
for i in a:
    if i > 0:
        b.append(i)
print('Положительные числа: ',b)
print('Максимальное положительное число: ',max(b))