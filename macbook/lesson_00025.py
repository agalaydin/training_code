# сумма цифр от 1 до n

var_1 = int(input("Введите число: "))
agregator = []
for i in range(1, var_1+1):
    print(i, sep=" ", end=" ")
    if i < var_1:
        print("+", sep=" ", end=" ")
    agregator.append(i)
print("=", sum(agregator))
