# генератор чисел Фибоначчи

def fibonacci(limit):       # генератор (а не функция, т.к. оператор return
    var_1, var_2 = 0, 1     # заменён на yield)        
    while var_1 < limit:        
        yield var_1         # return a, + запоминаем место рестарта для следующего вызова
        var_1, var_2 = var_2, var_1 + var_2 # параллельное присваивание, которое выполняется одновременно и параллельно

for n in fibonacci(1000):
    print(n, end=' ')
