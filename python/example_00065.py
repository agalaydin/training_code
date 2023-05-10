i = int(input())

if i / 2:
    print("1.", i, 'чётное')
else:
    print("1.", i, 'нечётное')

if i // 2:
    print("2.", i, 'чётное')
else:
    print("2.", i, 'нечётное')

if i % 2 == 0:
    print("3.", i, 'чётное')
else:
    print("3.", i, 'нечётное')

if i // 2 == 0:
    print("4.", i, 'чётное')
else:
    print("4.", i, 'нечётное')

if i % 2 != 0:
    print("5.", i, 'нечётное')
else:
    print("5.", i, 'чётное')

if i // 2 != 0:
    print("6.", i, 'нечётное')
else:
    print("6.", i, 'чётное')


