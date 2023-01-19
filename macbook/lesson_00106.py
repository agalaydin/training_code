def letter_frequency(in_string):
    frequencies = {}

    for i in in_string:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

freqs = letter_frequency("This is just a test string")

print(freqs)

