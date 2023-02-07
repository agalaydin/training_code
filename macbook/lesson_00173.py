# При вызове функции можно использовать оператор * для распаковки
# итерируемого объекта в аргументы вызова:

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits[0], fruits[1], fruits[2], fruits[3])
print(*fruits)
print(fruits)
