colors = ["фиолетовый", "оранжевый", "зелёный"]
guess = input("Угадайте цвет:")

if guess in colors:
    print("Вы угадали!")
else:
    print("Неправильно! Попробуй ещё.")
