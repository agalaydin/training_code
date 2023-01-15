var_1 = 15
var_2 = 30
print('var_1:', var_1, 'var_2:', var_2)
var_temp = var_1
var_1 = var_2
var_2 = var_temp
print('var_1:', var_1, 'var_2:', var_2)

print("\n")

var_1, var_2 = 45, 60
print('var_1:', var_1, 'var_2:', var_2)
var_1, var_2 = var_2, var_1
print('var_1:', var_1, 'var_2:', var_2)
