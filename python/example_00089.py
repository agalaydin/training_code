year = int(input())
if year == 1 or year == 3 or year == 5 or year == 7 or year== 8 or year == 10 or year == 12:
    print(31)
elif year == 4 or year == 6 or year == 9 or year == 11:
    print(30)
else:
    print(28)
