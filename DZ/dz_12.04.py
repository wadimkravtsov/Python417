sps = []
summ = 0


def my_decorator(func):
    def inner(sps):
        func(sps)
        print('Среднее арифметическое чисел', *sps, '=', sum(sps) / len(sps))
    return inner


@my_decorator
def plus(sps):  # Печать списка и подсчет суммы чисел
    summ = sum(sps)
    print('Сумма чисел', *sps, '=', summ)


print("Введите числа, 'Enter' - конец ввода.")
while True:
    sps_numb = input()
    if sps_numb == '':
        break
    else:
        sps.append(int(sps_numb))


plus(sps)
