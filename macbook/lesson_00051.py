def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input("Enter the year: "))

if is_leap(year):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
