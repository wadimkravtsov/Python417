
numb=int(input('Введите пятизначное число: '))
# numb=97531
a=numb%10
numb=numb//10
b=numb%10
numb=numb//10
c=numb%10
numb=numb//10
d=numb%10
numb=numb//10
e=numb
sr=(a+b+c+d+e)/5
mult=a*b*c*d*e
# print('Введите пятизначное число: 97531')
print('Произведение цифр числа: ',mult)
print('Среднее арифметическое: ',sr)