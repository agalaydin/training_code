my_list = [1, 2, 3, 4, 5, 6, 7]
print("[0:-3]", my_list[0:-3])
print("[0:3]+[8, 9]", my_list[0:3] + [8, 9])
print("[3, '4'] * 3", [3, '4'] * 3)

my_list[2] = "New"
print("my_list after change =", my_list)

my_list[0:3] = [5, 5, 5]
print("my_list[0:3] = [5, 5, 5]", my_list)

