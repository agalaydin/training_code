a = input("введите число: ")
b = input("введите ещё одно число: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b не может быть нулём.")
