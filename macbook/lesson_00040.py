# условные обозначения str() и repr() (!r и !s) c format()

# как и __format__() можно запросто переопределять методы
# __str__() и __repr__() объекта.

# __str__() и __repr__() сокращенно !s и !r
# реализация для класса __str__() и __repr__()

class MyClass:
    def __init__(self):
        self.my_str_var = 'Пайтон', 'Python'

    def __str__(self):
        return self.my_str_var[0]

    def __repr__(self):
        return self.my_str_var[1]
    

print("Лучший язык программирования: {!r}".format(MyClass()))
print("Лучший язык программирования: {!s}".format(MyClass()))
