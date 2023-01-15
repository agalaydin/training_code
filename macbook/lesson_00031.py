# объединяем два словаря

def merge(dic_1, dic_2):
    dic_3 = dic1.copy()
    dic_3.update(dic_2)
    return dic_3

dic1 = {1: "Hello", 2: "pythoninfo"}
dic2 = {3: "Python", 4: "is awesome",}
print(merge(dic1, dic2))
