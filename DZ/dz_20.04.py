import re

pwd  = input('Введите пароль:')
print(pwd)
reg = r"[A-Za-z0-9_@-]{6,18}"
res = (re.fullmatch(reg,pwd))
if res == None:
    print('Неверный ввод')
else:
    print(f'Пароль {res[0]} принят')
