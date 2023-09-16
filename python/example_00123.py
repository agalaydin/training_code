"""Python in 7 hours."""

x = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
y = input('Ввелите строку: ')

for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
        print('Букв', i, 'было', count)
