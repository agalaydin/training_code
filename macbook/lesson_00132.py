def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

numbers = [1, 2, 3, 4, 5]

sum = total(numbers)

print(sum)
