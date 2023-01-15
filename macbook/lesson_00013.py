# написание числа в обратном порядке

var_1 = int(input("Ведите чило: "))
reverse = 0
while var_1 > 0:
    rest = var_1 % 10
    reverse = reverse * 10 + rest
    var_1 = var_1 // 10
print("Число в обратном поярдке:", reverse)
