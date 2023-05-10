tv = ["Во все тяжкие",
     "Секретные материалы",
     "Фарго"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)
