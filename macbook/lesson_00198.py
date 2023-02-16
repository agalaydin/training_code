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

