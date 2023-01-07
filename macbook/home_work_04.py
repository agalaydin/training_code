fruits = ["яблоко", "банан", "киви", "арбуз"]
for count, value in enumerate(fruits, start=1):
    print(f'{count}.{value}')
print(fruits)
#fruits = sorted(fruits.items(), key=lambda x: x[-1])
#for key, value in d:
#    print('{0:>10} {1:<2}'.format(key, value))
