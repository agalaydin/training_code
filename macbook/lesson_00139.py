def find(target):
    for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"{number} in inspection...")
        if number == target:
            print("Target found!")
            break

find(3)
