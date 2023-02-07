# Объединение словарей до Python 3.9

a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {1:'fish', 2:'chips'}         

x = {**a, **b}
print(x)
