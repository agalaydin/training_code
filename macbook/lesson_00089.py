my_list = [1, 1, 2, 5, 10, 10, 10]
my_set = set(my_list)
s = 0
for el in my_set:
    s += el
print(s)

print(sum(set(my_list)))
