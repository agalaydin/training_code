# расстояние между двумя точками

from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

start = (1, 1)
end = (2, 2)

dist = distance(start, end)

print(f"The distance between {start} and {end} is {dist}")
