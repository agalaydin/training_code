"""Python in 7 hours."""

x = ''

while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue
    if y == 'l':
        break

    x += y

else:
    print(x)

print('Программа работает дальше')
