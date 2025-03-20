import numpy as np
import matplotlib.pyplot as plt


# Определим функцию и её производные
def f(x):
    return np.log(x ** 2 + 1)


def f_prime(x):
    return (2 * x) / (x ** 2 + 1)


def f_double_prime(x):
    return (2 * (1 - x ** 2)) / (x ** 2 + 1) ** 2


# Параметры сетки
a, b = -4, 4  # Интервал [a, b]
N = 100  # Количество узлов сетки
h = (b - a) / N
x = np.linspace(a, b, N)
F = f(x)


# Реализация функций для первой производной
def diff_1_right(F, h):
    return (np.roll(F, -1) - F) / h


def diff_1_central(F, h):
    return (np.roll(F, -1) - np.roll(F, 1)) / (2 * h)


# Реализация функций для второй производной
def diff_2_ord2(F, h):
    return (np.roll(F, -1) - 2 * F + np.roll(F, 1)) / h ** 2


def diff_2_ord4(F, h):
    return (-np.roll(F, -2) + 16 * np.roll(F, -1) - 30 * F + 16 * np.roll(F, 1) - np.roll(F, 2)) / (12 * h ** 2)


# Вычисление производных
F_prime_right = diff_1_right(F, h)
F_prime_central = diff_1_central(F, h)
F_double_prime_ord2 = diff_2_ord2(F, h)
F_double_prime_ord4 = diff_2_ord4(F, h)

# Визуализация первой производной
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, f_prime(x), label="Точная производная")
plt.plot(x, F_prime_right, '--', label="Правая разность")
plt.plot(x, F_prime_central, '--', label="Центральная разность")
plt.legend()
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Первая производная')

# Визуализация второй производной
plt.subplot(1, 2, 2)
plt.plot(x, f_double_prime(x), label="Точная вторая производная")
plt.plot(x, F_double_prime_ord2, '--', label="Второй порядок")
plt.plot(x, F_double_prime_ord4, '--', label="Четвертый порядок")
plt.legend()
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.title('Вторая производная')
plt.show()


# Анализ погрешности
def compute_error(F_num, F_exact):
    return np.max(np.abs(F_num - F_exact))


# Различные шаги сетки
steps = [2 ** i for i in range(4, 12)]
errors_right = []
errors_central = []
errors_ord2 = []
errors_ord4 = []

for N in steps:
    h = (b - a) / N
    x = np.linspace(a, b, N)
    F = f(x)

    # Первая производная
    F_prime_right = diff_1_right(F, h)
    F_prime_central = diff_1_central(F, h)
    F_prime_exact = f_prime(x)

    # Вторая производная
    F_double_prime_ord2 = diff_2_ord2(F, h)
    F_double_prime_ord4 = diff_2_ord4(F, h)
    F_double_prime_exact = f_double_prime(x)

    # Погрешности
    errors_right.append(compute_error(F_prime_right[:-1], F_prime_exact[:-1]))
    errors_central.append(compute_error(F_prime_central[1:-1], F_prime_exact[1:-1]))
    errors_ord2.append(compute_error(F_double_prime_ord2[1:-1], F_double_prime_exact[1:-1]))
    errors_ord4.append(compute_error(F_double_prime_ord4[2:-2], F_double_prime_exact[2:-2]))

# Визуализация погрешностей
plt.figure(figsize=(12, 6))
plt.loglog(steps, errors_right, 'o-', label="Правая разность (первая производная)")
plt.loglog(steps, errors_central, 'o-', label="Центральная разность (первая производная)")
plt.loglog(steps, errors_ord2, 'o-', label="Второй порядок (вторая производная)")
plt.loglog(steps, errors_ord4, 'o-', label="Четвертый порядок (вторая производная)")
plt.xlabel('Число узлов сетки')
plt.ylabel('Погрешность')
plt.title('Зависимость погрешности от шага сетки')
plt.legend()
plt.grid(True)
plt.show()

# Оценка оптимального шага сетки
epsilon = 1e-16  # Машинная точность
M = 2  # Максимальное значение третьей производной (для первой производной)
optimal_step = np.sqrt(epsilon / M)
print(f"Оптимальный шаг сетки: {optimal_step}")