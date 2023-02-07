a = {1:'peanut', 2:'butter', 3:'jelly', 4:'time'}
b = {1:'fish', 2:'chips'}         
c = {1: ['peanut','butter','jelly','time'], 2:['fish','chips']}
d = {1: ['fish','chips'], 2:['peanut','butter','jelly','time']}

my_dict = a | b # python 3.9+
print(my_dict)

my_dict_2 = {**a, **b, **c, **d}
print(my_dict_2)
