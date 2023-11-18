import math

point_a = [3, 4, 5]
point_b = [1, 3, 5]

addition = (
    (point_a[0] - point_b[0]) ** 2
    + (point_a[1] - point_b[1]) ** 2
    + (point_a[2] - point_b[2]) ** 2
)

distance = math.sqrt(addition)

print(distance)
