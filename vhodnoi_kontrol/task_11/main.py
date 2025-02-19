import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
a, b, c, d, e = sp.symbols('a b c d e')
y = a*x**4 + b*x**3 + c*x**2 + d*x + e
y = y.subs({a: 1, b: -6, c: 11, d: -6, e: 0}) #ввод значений a, b, c, d, e
y_prime = sp.diff(y, x)
critical_points = sp.solve(y_prime, x)
y_double_prime = sp.diff(y_prime, x)
def determine_point_type(point):
    second_deriv_at_point = y_double_prime.subs(x, point).simplify()
    if second_deriv_at_point > 0:
        return "минимум"
    elif second_deriv_at_point < 0:
        return "максимум"
    else:
        return "требуется дополнительный анализ"
minima = []
maxima = []
for point in critical_points:
    point_type = determine_point_type(point)
    if point_type == "минимум":
        minima.append(point)
    elif point_type == "максимум":
        maxima.append(point)
    print(f"Критическая точка: x = {point}, тип: {point_type}")
y_numeric = sp.lambdify(x, y, "numpy")
x_vals = np.linspace(min(critical_points) - 3,max(critical_points) + 3, 500)
y_vals = y_numeric(x_vals)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f"y = {a}x⁴ + {b}x³ + {c}x² + {d}x + {e}", color="blue")
for point in minima:
    plt.scatter(point, y_numeric(point), color="red", zorder=5, label=f"Минимум: x = {point:.2f}")
for point in maxima:
    plt.scatter(point, y_numeric(point), color="green", zorder=5, label=f"Максимум: x = {point:.2f}")
plt.title("График функции y = ax⁴ + bx³ + cx² + dx + e")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.grid(True)
plt.legend()
plt.show()

