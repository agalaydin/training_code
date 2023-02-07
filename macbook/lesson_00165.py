import operator

# слияние двух словарей в один в Python 3.9 и выше

a = {'a':500, 'b':600, 'c':700}
b = {'d':400, 'e':300, 'f':200, 'g':100}
d = a | b
print(d)

# Сортировка по значению

result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)


