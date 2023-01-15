# проверка дубликатов

def check_duplicate(lst):
    return len(lst) != len(set(lst))

print(check_duplicate([51, 37, 3, 45, 5, 49, 77]))
print(check_duplicate([1, 3, 3]))
print(check_duplicate([11, 2, 88, 4, 16]))
