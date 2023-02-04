import operator

# отсортируйте словарь по значению в порядке возрастания и убывания

d = {'a':500, 'b':600, 'c':700, 'd':400, 'e':300, 'f':200, 'g':100}

result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)


