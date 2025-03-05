import random

A = B = 10
R = 1
X0 = Y0 = 5
N = 100000

def f():
    count_inside = 0
    for _ in range(N):
        x = random.uniform(0, A)
        y = random.uniform(0, B)
        if (x - X0) ** 2 + (y - Y0) ** 2 <= R ** 2:
            count_inside += 1

    area_rectangle = A * B
    area_circle = (count_inside / N) * area_rectangle

    return area_circle

areas = []
for _ in range(10):
    area = f()
    areas.append(area)

mean_area = sum(areas) / len(areas)
variance_area = sum((x - mean_area) ** 2 for x in areas) / len(areas)

print("Математическое ожидание площади круга:", mean_area)
print("Дисперсия площади круга: ", variance_area)