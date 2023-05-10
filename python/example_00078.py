n = int(input())
if 999 < n < 10000:
    if n % 7 == 0 or n % 17 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
