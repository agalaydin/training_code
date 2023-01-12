a = list()
a.append(int(input("Введите пераое число: ")))
a.append(int(input("Введите второе число: ")))
a.append(int(input("Введите третье число: ")))
s = 0
for i in a:
    if i >= 0:
        s += i
print(s)
