# Сложите цифры целого числа
NUM = 12345

# Вариант решения 1 - пользуемся циклом for
def sum_for(num):
    # Инициализируем переменную для суммы
    s = 0
    # Преобразуем число в строку
    # В цикле перебираем символы полученной строки
    for item in str(num):
        # Каждый символ переводим в число и добавляем к сумме
        s = s + int(item)
    # Возвращаем конечную сумму
    return s

# Вариант решения 2 - используем генераторы списков
def sum_list(num):
    # Создаем список с помощью генератора
    # Конечные элементы списка переводим в числа
    lst = [int(item) for item in str(num)]
    # С помощью встроенной функции sum() находим сумму элементов списка
    return sum(lst)

# Тесты
if __name__ == '__main__':
    print(sum_for(NUM))
    print(sum_list(NUM))

