num=int(input('Введите число от 1 до 99: '))
if 0<num<100:
    print(num, end=' ')
    if 9<num<20:
        # print('копеек')
        ort=5
    elif 0<num<=9:
        ort=num
    else:
        ort=num%10
    if ort==1:
        print('копейка')
    if 1<ort<5:
        print('копейки')
    if 4<ort<10 or ort==0:
        print('копеек')
else:
    print('ошибка ввода')