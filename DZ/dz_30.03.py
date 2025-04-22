base = {
    'John':{
        'N':2054,
        'S':3677,
        'E':5600,
        'W':3355
    },
    'Tom':{
        'N':1150,
        'S':3680,
        'E':3600,
        'W':3390
    },
    'Anne':{
        'N':2070,
        'S':3689,
        'E':5602,
        'W':3355
    },
    'Fiona':{
        'N':2000,
        'S':3600,
        'E':5605,
        'W':3325
    }
}
for i in base:
    print(i)
    for j in base[i]:
        print(j,':',base[i][j])

name = input('Имя: ')
reg = input('Регион: ')
print(base[name][reg])
base[name][reg] = int(input('Новое значение: '))
print(base[name])