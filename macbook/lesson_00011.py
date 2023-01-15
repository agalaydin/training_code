#===================
#   Set (множество)
#===================

# Множество - контейнер, содержащий не повторяющиеся элементы в случайном порядке.

a = set()
print('a =', a)

b = set(['a', 'b', 'c', 'c', 'a', 'e'])
print('b = ', b)

c = set('hello')
print('c =', c)

d = {'a', "b", "c", "d"}
print("d = ", d)

e = {i ** 2 for i in range(10)}
print("e = ", e)

f = {} # так получится словарь
print("type({}) -->", type(f))

# операции с множествами

print(len(e))
print("'b' in b -->", 'b' in b)

# s == t
c1 = {"e", "l", "o", "h"}
print(c == c1)

# s.issubset(t) s <= t
print(c <= c1)


# s.issuperset(t) s >= t
print(c >= {"h"})

# s.union(t, ...) s | t
print(b | d)

# s.intersection(t, ...) s & t
print(d - b)

# s.difference(t, ...) s - t 

# s.symmetric_difference(t) s ^ t
print(d ^ b)

# s.copy()
f = e
g = e.copy()
print("e:", id(e))
print("f:", id(f))
print("g:", id(g))

# методы, изменяющие множества

# s.update(other, ...) s |= t
b |= d
print(b)

# s.intersection_update(t) s ^= t
b ^= c
print(b)

# s.add(elem)
b.remove("h")
print(b)
b.discard("z")

# s.pop()
print(b.pop())
print(b)

#===================
# Frozeset (неизменяемые множества)
a = frozenset("hellow")
b = set("hellow")
print(a == b)
print(type(a - b))
print(type(b | a))
b.add("q")
# a.dd("q") # вызовет ошибку
