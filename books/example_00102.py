# Фиьтрация значений False

# Этот пример используется для устранения всех ложных значений из списка,
# например false, 0, None, " ".

def Filtering(lst):
    return list(filter(None,lst))
lst = [None, 1, 3, 0, "", 5, 6, 7]
print(Filtering(lst))
