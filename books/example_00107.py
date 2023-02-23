# Сортировка словаря

orders = {
    'pizza': 200,
    'burge': 56,
    'pepsi': 25,
    'coffe': 14
}

sorted_dic = sorted(orders.items(), key=lambda x: x[1])
print(sorted_dic)
