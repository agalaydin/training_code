try:
    a = input("введите число: ")
    b = input("введите ещё одно число: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("ошибка ввода.")
