items = ["Alice", 2, 3, "Bob", "Chaarlie", 30]

# Let's remove numbers

names = filter(lambda x: not isinstance(x, int), items)

print(list(names))
