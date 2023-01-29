print("Задача № 1")

n = int(input("Введите число до 1000: "))

if n < 10:
    print(n)
if n >= 10 and n < 100:
    print(n//10)
    print(n%10)
if n >= 100 and n < 1000:
    print(n//100)
    print((n%100) // 10)
    print(n%10)
if n >= 1000 and n < 10000:
    print(n//1000)
    print((n%1000) // 100)
    print((n%1000) % 100 // 10)
    print(n%10)

print("Задача № 2\n")

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

print("x = ", x)
print("y = ", y)
z = x
x = y
y = z
print("Меняем местами значение переменных")
print("x = ", x)
print("y = ", y)

print("Задача № 3\n")

age = int(input("Введите ваш возраст: "))
if age > 17:
    print("Доступ разрешёт")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
