# пользовательский мметод __format__()

class MyClass:
    def __init__(self):
        self.my_str_var = 'Пайтон'


    def __format__(self, format):
        if (format == 'Python'):
            return self.my_str_var
        else:
            return self.my_str_var

print("Лучший язык программирования: {:Python}".format(MyClass()))
