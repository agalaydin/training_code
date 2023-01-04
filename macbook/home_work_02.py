import math

print("Задача № 1")

n = input("Введите число: ")
m = n
n = int(n)
v = 0
while n > 0:
    g = n % 10
    if g > v:
        v = g
    n //= 10
print("Вариант с while. Наибольшая цифра в числе", m, ":", v)

k = 0
for i in m:
    i = int(i)
    if i > k:
        k = i
print("Вариант с for. Наибольшая цифра в числе", m, ":", k)

print("Задача № 2")

n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))

print("x =", n1)
print("y =", n2)
print("Меняем местами значения переменных")
print("x =", n1-(n1-n2))
print("y =", (n1-n2)+n2)

print("Задача № 3")

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("Введите a:"))
b = float(input("Введите b:"))
c = float(input("Введите c:"))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2*a)
    print("x = %.2f" %x)
else:
    peint("Корней нет")


