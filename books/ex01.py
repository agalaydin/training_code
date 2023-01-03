l = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
index = -2
result = " ".join(l)
result = result[:index] + result[index+1:]
print(result)
