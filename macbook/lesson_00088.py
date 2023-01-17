def my_func(input_set, input_list):
    if len(input_list) > len(input_set):
        return False
    
    for list_el in input_list:
        if list_el not in input_set:
            return False
    return True
print(my_func({1, 2, 3, 4, 5, "Hello"}, [5]))
print(my_func({1, 2, 3, 4}, [5]))
