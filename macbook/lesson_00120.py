def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numbers = flatten(matrix)

print(numbers)
