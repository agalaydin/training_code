# проверить, является ли слово палиндромом
# вариант получше:

var_1 = 'level'
ispalindrome = var_1 == var_1[::-1]
if ispalindrome:
    print('Palindrome')
else:
    print('Simp;e word')
