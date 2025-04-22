n,symbol,orient = input("Введите через запятую: количество символов, символ и ориентацию (0 - строка, 1 - колонка): ").split(",")
n = int(n)
i = 0
while i<n:
    if orient == "0":
        print(symbol, end=" ")
    elif orient == "1":
        print(symbol)
    else:
        print("Неверный ввод")
        break
    i += 1