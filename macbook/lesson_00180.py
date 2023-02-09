# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо 
# и справа налево

def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('abba'))
