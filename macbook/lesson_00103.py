def intersection(n1, n2):
    return [element for element in n1 if element in n2]

names1 = ["Alice", "Bob", "Charlie"]
names2 = ["Alice", "Bob", "Charlie", "David", "Emma"]

names_in_common = intersection(names1, names2)

print(f"Common names among the list are {names_in_common}")
