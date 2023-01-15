# получаем гласные

def get_vowels(word):
    return [each for each in word if each in "aeiouy"]
print(get_vowels("animal"))
print(get_vowels("sky"))
print(get_vowels("football"))
