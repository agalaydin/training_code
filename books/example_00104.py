# Занять память

# Пример позволяет получить объём памяти, используемой любой переменной
# в Python

import sys
var1 = "Python"
var2 = 100
var3 = True
print(sys.getsizeof(var1))
print(sys.getsizeof(var2))
print(sys.getsizeof(var3))
