# Анаграммы

# Этот код полезен для проверки тогоБ является ли строка анаграммой.
# Анаграмма - это слово, полученное перестановкой букв другого слова.


from collections import Counter
def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
print(anagrams("abc1", "1bac"))
