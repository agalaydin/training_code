#============================
#        Dict (словарь)
#============================

print('-= dict =-')

# Словарь - неупорядрченная коллекция произвольных объектов с доступом по ключу.

a = {}
print('a =', a)

b = {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}
print('b =', b)

# Создание с помощью функции dict:
c = dict(key='val',  spam='eggs')
print('c =', c)

d = dict([(1, 10), (2, 20)])
print('d =', d)

# Создание словаря с помощью метода fromkeys:
e = dict.fromkeys(['a', 'b', 'c'])
print('e =', e)

f = dict.fromkeys(['a', 'b', 'c'], 'initial')
print('f =', f)

# Cоздание словаря с помощью генератора:
g = {i: i ** 2 for i in range(10)}
print('g =', g)

# Доступ к элементу
print("f['a'] -->", f['a'])

f['b'] = 'spam'
f['c'] = 'eggs'
print('f_change =', f)
# f['from']  # обращение к несуществующему ключу вызовет исключение

# Удаление элемента
del f['b']

# Операции со словарём

# Кол-во элементов
print('len(f) -->', len(f))
print(f)

# Проверим, есть ли данный ключ
if 'a' in f:
    print("a in f")

if 'a' not in f:
    print('a not in f')

if not 'a' in f:
    print('a not in f')

print("f.get('d', 'eggs') -->", f.get('d', 'eggs'))

# Цикл по словарю
for key, value in f.items():
    print(key, value)

for key in f.keys():
    print(key)

for value in f.values():
    print(value)

# Удаляет и возвращает пару (ключ, значение)
print(f.pop('c'))
print(f)

# Удаляет и возвращает пару (ключ, значение)
print(f.popitem())

print(f.setdefault('x', 'spam'))
print(f)

# Вывод отсортированных по ключу пар ключ/значение
d = {'a': 'alpha', 'b': 'beta', 'g': 'gamma'}
print(d)
for key in sorted(d.keys()):
    print(key, d[key])

# Вывод пар ключ/значение, отсортированных по значению
d = {'one': 10, 'more': 5, 'thing': 11}
d = sorted(d.items(), key=lambda x: x[-1])
for key, value in d:
    print('{0:>10} {1:<2}'.format(key, value))
