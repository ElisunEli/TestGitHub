import math

def distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def comp_distance(p1, p2, p3):
    return distance(p1, p2) == (distance(p2, p3)+distance(p1, p3))

p1 = [4, 0]
p2 = [6, 0]
p3 = [5, 0]
print(comp_distance(p1, p2, p3))

p1 = [1, 1]
p2 = [2, 2]
p3 = [1.5, 1.5]
print(comp_distance(p1, p2, p3))
