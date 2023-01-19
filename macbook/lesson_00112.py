def mul_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

n = int(input("Enter a number: "))
mul_table(n)
