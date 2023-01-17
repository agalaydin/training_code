data = {"имя": "Артём",
        "рост": 174,
        "вес": 77
       }

answer = input("Укажите имя, рост или вес: ")
if answer in data:
    result = data[answer]
    print(result)
