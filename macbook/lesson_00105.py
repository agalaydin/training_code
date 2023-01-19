def as_pounds(kilos):
    return 2.2048 * kilos

kg = int(input("Enter a kg: "))
pounds = as_pounds(kg)

print(f"{kg} is {pounds} in pounds")
