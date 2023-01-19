num_strs = input("Give a comma-separated numbers: ")
print("num_strs =", num_strs)

num_str_list = num_strs.split(",")
print("num_str_list =", num_str_list)

num_ints = [int(num_str) for num_str in num_str_list]
print("num_ints =", num_ints)

reversed_nums = list(reversed(num_ints))
print(reversed_nums)
