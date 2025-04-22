s ='Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'
first = s.find('о')
second = s.rfind('о')
str = s[:first + 1] + s[first + 1:second].replace('о','О') + s[second:]
print(str)