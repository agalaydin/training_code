def as_fahrenheit(celsius):
    return 9/5 * celsius + 32

c = int(input("Enter degrees celsius: "))
f = as_fahrenheit(c)

print(f"{c} is {f} in Fahrenheits")
