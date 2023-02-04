# нужно вернуть список, который состоит из элементов,
# общих для этих двух списков

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ab = []
for n in a:
    for m in b:
        if n == m:
            ab.append(m)
ab = set(ab)
print(ab)

# функция filter

result = list(filter(lambda elem: elem in b, a))
print(result)
