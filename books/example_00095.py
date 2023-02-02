# получаем гласные

# этот пример возвращает в строке найденные гласные "a e i o u"
# это может оказаться полезным при поиске или обнаружении гласных

def get_vowels(String):
    return [each for each in String if each in "aeiou"]
s1 = get_vowels("animal") # [a, i, a]
s2 = get_vowels("sky") # []
s3 = get_vowels("football") # [o, o, a]
print(s1)
print(s2)
print(s3)
