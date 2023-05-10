# Вычисляем время выполнения

# Этот пример полезен, когда вам нужно знать, сколько временни требуется для
# выполнения программы или функции

import time
start_time = time.time()
def fun():
    a = 2
    b = 3
    c = a + b
end_time = time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)
