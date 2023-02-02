n = int(input())
if n == 0:
    print("зеленый")
elif 0 < n <= 10 or 19 <= n <= 28:
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= n <= 18 or 29 <= n <= 36:
    if n % 2 == 0:
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")
