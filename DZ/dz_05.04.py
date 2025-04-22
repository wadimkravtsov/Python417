students = {}
n = int(input('Введите количество студентов: '))
for i in range(n):
    name,num = input('Введите через запятую имя студента и его балл: ').split(',')
    students[name] = num
print('\nКоличество студентов: ',n)
i = 1
sum = 0
for student in students:
    print(i,'-й студент: ',student, sep='')
    print('Балл:',students[student])
    i += 1
    sum += int(students[student])
average = round(sum/n)
# print(sum,average)
print('\nСредний балл: ',average,'. Студенты с баллом выше среднего: ',sep='')
for student in students:
    if int(students[student]) > average:
        print(student)