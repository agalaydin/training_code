from datetime import date

d1 = date(2023, 1, 19)
d2 = date(2024, 1, 1)

diff = (d2 - d1).days

print(f"The difference between {d1} and {d2} is {diff} days")
