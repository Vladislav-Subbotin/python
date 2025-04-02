import numpy as np


def ray_crossing_method(p, T1, T2, T3):
    """Проверяет, лежит ли точка p внутри треугольника T1T2T3 методом трассировки луча."""
    x, y = p
    x1, y1 = T1
    x2, y2 = T2
    x3, y3 = T3

    # Функция проверки пересечения луча (y = const) с отрезком (A, B)
    def ray_intersects_segment(A, B):
        (Ax, Ay), (Bx, By) = A, B

        # Если отрезок горизонтальный и лежит на луче → точка на границе
        if Ay == By == y:
            return (min(Ax, Bx) <= x <= max(Ax, Bx))

        # Если точка выше или ниже отрезка → нет пересечения
        if (Ay > y and By > y) or (Ay < y and By < y):
            return False

        # Если точка справа от обоих концов отрезка → нет пересечения
        if x >= max(Ax, Bx):
            return False

        # Если точка слева от обоих концов → пересечение возможно
        if x < min(Ax, Bx):
            return True

        # Проверяем пересечение с помощью уравнения прямой
        # (x - Ax) / (Bx - Ax) = (y - Ay) / (By - Ay)
        if Bx != Ax:
            x_intersect = Ax + (y - Ay) * (Bx - Ax) / (By - Ay)
        else:
            x_intersect = Ax

        return x <= x_intersect

    # Проверяем все три ребра
    edges = [
        ((x1, y1), (x2, y2)),
        ((x2, y2), (x3, y3)),
        ((x3, y3), (x1, y1))
    ]

    intersections = 0
    for A, B in edges:
        if ray_intersects_segment(A, B):
            # Если точка лежит на ребре → сразу возвращаем True
            if (min(A[0], B[0]) <= x <= max(A[0], B[0])) and (min(A[1], B[1]) <= y <= max(A[1], B[1])):
                # Проверка коллинеарности (точка на прямой)
                area = (B[0] - A[0]) * (y - A[1]) - (B[1] - A[1]) * (x - A[0])
                if abs(area) < 1e-10:
                    return True
            intersections += 1

    return intersections % 2 == 1


def monte_carlo_triangle_area(T1, T2, T3, A, B, N=10000, iterations=10):
    areas = []
    S_rect = A * B

    for _ in range(iterations):
        points = np.random.rand(N, 2) * [A, B]
        K = 0

        for p in points:
            if ray_crossing_method(p, T1, T2, T3):
                K += 1

        S_est = (K / N) * S_rect
        areas.append(S_est)

    return areas


# Пример использования:
T1 = (1, 1)
T2 = (4, 1)
T3 = (2, 5)
A, B = 5, 5  # прямоугольник [0,5]x[0,5]

estimates = monte_carlo_triangle_area(T1, T2, T3, A, B)
print("Оценки площадей за 10 попыток:", estimates)
print("Матожидание:", np.mean(estimates))
print("Дисперсия:", np.var(estimates))