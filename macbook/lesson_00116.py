def get_factors(x):
    return [i for i in range(1, x+1) if x % i == 0]

number = 460
factors = get_factors(number)

print(factors)
