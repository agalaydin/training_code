a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвёртое число: "))

"""
if a < b:
    if a < c:
        if a < d:
            print(a, "наименьшее число.")
        else:    
            print(d, "наименьшее число.")
    if c < a:
        if c < d:
            print(c, "наименьшее число.")
        else:
            print(d, "наименьшее число.")
if b < a:
    if b < c:
        if b < d:
            print(b, "наименьшее число.")
        else:    
            print(d, "наименьшее число.")
    if c < b:
        if c < d:
            print(c, "наименьшее число.")
        else:
            print(d, "наименьшее число.")
"""

if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)
