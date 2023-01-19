def pyramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1) + "*"*(2*i+1))

n = int(input("Enter a number: "))
pyramid(n)
