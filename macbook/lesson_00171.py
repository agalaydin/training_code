
# -*- coding: utf-8 -*-
'''
Добавление значений списка во все версии Python
Добавление вложеных значений, а не перезапись
Это можно сделать, используя метод extend()
'''
a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {1:'fish', 2:'chips'}         
c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}

for k, v in d.items():
    if k in c:
        c[k].extend(v)
    else:
        c[k] = v
print(c)
