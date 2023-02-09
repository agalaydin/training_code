# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо 
# и справа налево

# сравниваем строку с её обратной версией, 
# для чего можно использовать встроенную функцию reversed

def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('abba'))

# используем срезы

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('abba'))
