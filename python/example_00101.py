# Проверка дубликатов

# Это самый быстрый способ проверки наличия повторяющих значений в списке

def check_duplicate(lst):
    return len(lst) != len(set(lst))
res = check_duplicate([1, 2, 3, 4, 5, 6, 4])
print(res)
