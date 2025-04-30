st = [-2, 3, 8, -11, -4, 6, 5, 6, 7, -16, 4, -34, -7]
def func(st):
    if st == []:
        return 0
    else:
        count = func(st[1:])
        if st[0] < 0:
            count += 1
            # print(count)
    return (count)
print(f'В массиве {func(st)} отрицательных чисел')