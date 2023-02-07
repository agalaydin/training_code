# -*- coding: utf-8 -*-
'''
Объединение словарей в Python 2
использование метода items()
для вложенного словаря, содержащего значения списка
items() вызов необходимо преобразовать в list()
'''
a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {1:'fish', 2:'chips'}         
c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}

y = dict(list(c.items() + list(d.items())))
print(y)
