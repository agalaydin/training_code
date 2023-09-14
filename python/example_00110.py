"""Тест."""

number1 = 5
number2 = 10
print(number1 + number2)

num1 = num2 = 5
print(num1, num2)

num_1, num_2 = 5, 7
print(num_1, num_2)

swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1
print(swap1, swap2)

swap3 = 10
swap4 = 25
swap3, swap4 = swap4, swap3 + swap4
print(swap3, swap4)

swap4 -= number1
print(swap4)
