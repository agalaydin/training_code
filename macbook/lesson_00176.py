# Слияние нескольких словарей

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
print(result)

# вариант со "звёздочками"

res = {**dict_a, **dict_b, **dict_c}
print(res)
