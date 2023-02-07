# Объединение словарей до python 3.9

c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}

y = {**c, **d}
print(y)
