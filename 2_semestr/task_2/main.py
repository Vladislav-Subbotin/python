import numpy as np

def ray_intersects_segment(p, a, b):
    if a[1] > b[1]:
        a, b = b, a
    if p[1] < a[1] or p[1] > b[1]:
        return False
    if p[1] == a[1] or p[1] == b[1]:
        return False
    x_intersect = (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1]) + a[0]
    return p[0] < x_intersect

def point_in_triangle_ray_casting(p, t1, t2, t3):
    count = 0
    count += ray_intersects_segment(p, t1, t2)
    count += ray_intersects_segment(p, t2, t3)
    count += ray_intersects_segment(p, t3, t1)
    return count % 2 == 1

def estimate_triangle_area(t1, t2, t3, A, B, num_points=10000):
    rectangle_area = A * B
    points = np.random.rand(num_points, 2) * np.array([A, B])
    inside = np.array([point_in_triangle_ray_casting(p, t1, t2, t3) for p in points])
    inside_count = np.sum(inside)
    return (inside_count / num_points) * rectangle_area
T1 = (1, 1)
T2 = (4, 1)
T3 = (2, 5)
A = 5
B = 6
num_estimates = 10
estimates = [estimate_triangle_area(T1, T2, T3, A, B) for _ in range(num_estimates)]
mean_area = np.mean(estimates)
variance_area = np.var(estimates)

print(f"Оценки площади: {estimates}")
print(f"Математическое ожидание площади: {mean_area}")
print(f"Дисперсия площади: {variance_area}")