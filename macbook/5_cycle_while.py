print("Первый цикл")

i = 1
while i < 5:
    if i < 2:
        print(i, " строка")
    if i < 5 and i > 1:
        print(i, " строки")
    i += 1

print("Второй цикл")

i = 0
while True:
    if i >= 6:
        break
    print(i)
    i += 1

print("Третий цикл")

i = 0
while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)
    
