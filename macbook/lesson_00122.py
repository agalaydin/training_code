def item_frequency(in_list):
    frequencies = {}

    for i in in_list:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

freqs = item_frequency(["Alice", "Bob", "Bob", "Charlie", "Bob"])

print(freqs)
