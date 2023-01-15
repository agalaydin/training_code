#Подбор элемментов по индексам
fruits = ['apple', 'banana', 'mango']
i = 0
while len(fruits) > i:
    print('fruit =', fruits[i])
    i += 1

for fruit in fruits:
    print("fruit =", fruit)
print()

for el in 'Hello':
    print('\n', el)
print()

for t_el in 1, 2, 3, 4, 5, 10:
    print("------------")
    print('t_el =', t_el)
print()

for el in [1, 2, 'Hello', 4]:
    print('el =', el)
    break
print()
