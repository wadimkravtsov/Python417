a = [input('=>') for i in range(int(input('Введите n: ')))]
print(a)
s = 0
count = 0
for i in a:
    i = int(i)
    s += i
    if i != 0:
        count += 1
print(s/count)