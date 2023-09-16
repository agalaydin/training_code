"""Python in 7 hours."""

m = 'stroka text'
count = 0

for i in 'stroka text':
    if i == 't':
        print('Встроке есть буква t')
        count += 1
    
    if i == 'a':
        break

else:
    print('Цикл завершен, букв t =', count)

print('Программа работает дальше')
