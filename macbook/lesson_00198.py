def calc(a, b, operation):
    # Задаём дефолтное значение возвращаемого результата
    result = 'Операция не поддерживается'

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        # Проверка деления на ноль
        if b is not 0:
            result = a / b
        else:
            result = 'Делить на 0 нельзя!'

    return result

if __name__ == '__main__':
    # Проверяем корректные значения
    print(calc(30, 15, '+'))
    print(calc(30, 15, '-'))
    print(calc(30, 15, '*'))
    print(calc(30, 15, '/'))
    # Проверяем проверку деления на ноль
    print(calc(30, 0, '/'))
    # Проверяем неподдерживаемую операцию
    print(calc(30, 15, '%'))
