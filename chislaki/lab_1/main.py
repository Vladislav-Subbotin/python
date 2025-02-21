import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (10 - np.cos(2 * x) + np.log(1 + x)) / (x + 10)

def lagrange_interpolation(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

def uniform_grid(a, b, N):
    return np.linspace(a, b, N)

def chebyshev_grid(a, b, N):
    k = np.arange(1, N + 1)
    x_cheb = np.cos((2 * k - 1) * np.pi / (2 * N))
    return 0.5 * (a + b) + 0.5 * (b - a) * x_cheb

def investigate_interpolation(a, b, N_values, grid_type='uniform'):
    errors = []
    for N in N_values:
        if grid_type == 'uniform':
            x_nodes = uniform_grid(a, b, N)
        elif grid_type == 'chebyshev':
            x_nodes = chebyshev_grid(a, b, N)
        y_nodes = f(x_nodes)

        x_star = (x_nodes[:-1] + x_nodes[1:]) / 2
        y_star = f(x_star)
        y_interp = np.array([lagrange_interpolation(x, x_nodes, y_nodes) for x in x_star])

        max_error = np.max(np.abs(y_star - y_interp))
        errors.append(max_error)

        plt.figure()
        x_plot = np.linspace(a, b, 1000)
        y_plot = f(x_plot)
        y_interp_plot = np.array([lagrange_interpolation(x, x_nodes, y_nodes) for x in x_plot])
        plt.plot(x_plot, y_plot, label='f(x)')
        plt.plot(x_plot, y_interp_plot, label='Interpolation')
        plt.scatter(x_nodes, y_nodes, color='red', label='Nodes')
        plt.title(f'Interpolation with {N} nodes ({grid_type} grid)')
        plt.legend()
        plt.show()

    plt.figure()
    plt.plot(N_values, errors, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of nodes (N)')
    plt.ylabel('Max error')
    plt.title(f'Max error vs N ({grid_type} grid)')
    plt.grid(True)
    plt.show()

a, b = 0, 10
N_values = [5, 10, 50, 100, 150]

investigate_interpolation(a, b, N_values, grid_type='uniform')

investigate_interpolation(a, b, N_values, grid_type='chebyshev')