x = 5
y = 10
temp = x
x = y
y = temp
print("x =", x, "y =", y)

x, y = y, x
print("x =", x, "y =", y)
