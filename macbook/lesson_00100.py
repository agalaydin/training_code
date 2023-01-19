def factorial(number):
    result = 1
    while number >= 1:
        result *= number
        number -= 1
    return result
f = int(input("Entera number: "))
print("factorial", f, "=", factorial(f))
