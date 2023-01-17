def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Не удалось преобразовать строку в число с плавующей точкой.")
x = input("Введите число: ")    
z = convert(x)
print(z)
