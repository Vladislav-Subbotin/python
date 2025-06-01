import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log
import random

mc2 = 0.511  # Энергия покоя электрона в МэВ
r0 = 2.818e-13  # Классический радиус электрона в см
Na = 6.022e23  # Число Авогадро

R = 5.0
D = 10.0
d = D / 2
X0, Y0, Z0 = 0, 0, 15
N = 100000
E_gamma = 0.662
n_channels = 1024
E_min, E_max = 0, 0.7
channel_width = (E_max - E_min) / n_channels

rho_NaI = 3.67
Z_Na, A_Na = 11, 23
Z_I, A_I = 53, 127

spectrum = np.zeros(n_channels, dtype=int)


def ray():
    while True:
        l = random.uniform(-1, 1)
        m = random.uniform(-1, 1)
        n = random.uniform(-1, 1)
        length = sqrt(l ** 2 + m ** 2 + n ** 2)
        if length <= 1:
            return l / length, m / length, n / length


def cross_cylinder(l, m, n, x0, y0, z0):
    a = l ** 2 + m ** 2
    b = 2 * (x0 * l + y0 * m + z0 * n)
    c = x0 ** 2 + y0 ** 2 - R ** 2
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None

    sqrtD = sqrt(D)
    t1 = (-b - sqrtD) / (2 * a)
    t2 = (-b + sqrtD) / (2 * a)

    t = None
    if t1 > 0 and t2 > 0:
        t = min(t1, t2)
    elif t1 > 0:
        t = t1
    elif t2 > 0:
        t = t2
    else:
        return None

    x = x0 + l * t
    y = y0 + m * t
    z = z0 + n * t

    if -d <= z <= d:
        return x, y, z, t
    return None


def cross_plane(l, m, n, x0, y0, z0, A, B, C, D):
    denominator = A * l + B * m + C * n
    if abs(denominator) < 1e-10:
        return None

    t = -(A * x0 + B * y0 + C * z0 + D) / denominator
    if t < 0:
        return None

    x = x0 + l * t
    y = y0 + m * t
    z = z0 + n * t
    return x, y, z, t


def inside_plane(x, y, z, plane_type):
    if plane_type == 'top':
        if abs(z - d) > 1e-6:
            return False
    else:
        if abs(z + d) > 1e-6:
            return False

    return sqrt(x ** 2 + y ** 2) <= R


def inside_cylinder(x, y, z):
    return (-d <= z <= d) and (sqrt(x ** 2 + y ** 2) <= R)


def length_free_path(sigma_total):
    return -log(random.random()) / sigma_total


def sigma_photo(E, Z):
    if E < 0.01:
        return 1e-30

    gamma = E / mc2
    sigma_K = 6.651e-25 * 4 * sqrt(2) * (Z ** 5) / (137 ** 4) * (1 / gamma) ** 3.5
    return 1.25 * sigma_K


def sigma_compton(E, Z):
    if E < 0.001:
        return 0

    gamma = E / mc2
    if gamma < 0.1:
        return 6.651e-25 * Z * 8 / 3

    term1 = 1 + 2*gamma
    term2 = (1 - (2 * (1 + gamma) / (gamma ** 2))) * log(term1)
    term3 = 1 / (2 * ((2 * gamma + 1) ** 2))
    sigma = 6.651e-25 * 3 * Z / (8 * gamma) * (1/2+ 4/gamma + term2 - term3)
    return sigma


def calculate_macroscopic_sigma(E):
    sigma_ph_Na = sigma_photo(E, Z_Na)
    sigma_ph_I = sigma_photo(E, Z_I)
    sigma_c_Na = sigma_compton(E, Z_Na)
    sigma_c_I = sigma_compton(E, Z_I)

    n_Na = rho_NaI * Na / (A_Na + A_I)
    n_I = n_Na

    mu_ph = n_Na * sigma_ph_Na + n_I * sigma_ph_I
    mu_c = n_Na * sigma_c_Na + n_I * sigma_c_I
    mu_total = mu_ph + mu_c

    return mu_ph, mu_c, mu_total


def compton_energy_loss(E, costheta):
    alpha = E / mc2
    return E * (1 - 1 / (1 + alpha * (1 - costheta)))


def get_channel(E):
    channel = int((E - E_min) / channel_width)
    if 0 <= channel < n_channels:
        return channel
    return None


A_top, B_top, C_top, D_top = 0, 0, 1, -d
A_bottom, B_bottom, C_bottom, D_bottom = 0, 0, 1, d

for _ in range(N):
    E = E_gamma
    l, m, n = ray()

    intersections = []

    cross = cross_plane(l, m, n, X0, Y0, Z0, A_top, B_top, C_top, D_top)
    if cross:
        x, y, z, t = cross
        if inside_plane(x, y, z, 'top'):
            intersections.append((x, y, z, t))

    cross = cross_plane(l, m, n, X0, Y0, Z0, A_bottom, B_bottom, C_bottom, D_bottom)
    if cross:
        x, y, z, t = cross
        if inside_plane(x, y, z, 'bottom'):
            intersections.append((x, y, z, t))

    cross = cross_cylinder(l, m, n, X0, Y0, Z0)
    if cross:
        x, y, z, t = cross
        intersections.append((x, y, z, t))

    if not intersections:
        continue

    intersections.sort(key=lambda x: x[3])
    x_entry, y_entry, z_entry, t_entry = intersections[0]

    while E > 0.001:
        mu_ph, mu_c, mu_total = calculate_macroscopic_sigma(E)
        if mu_total < 1e-10:
            break
        L = length_free_path(mu_total)

        x_int = x_entry + l * L
        y_int = y_entry + m * L
        z_int = z_entry + n * L

        if not inside_cylinder(x_int, y_int, z_int):
            break

        r = random.random()
        if r < mu_ph / mu_total:
            channel = get_channel(E)
            if channel is not None:
                spectrum[channel] += 1
            break
        else:
            costheta = 2 * random.random() - 1
            E_loss = compton_energy_loss(E, costheta)

            channel = get_channel(E_loss)
            if channel is not None:
                spectrum[channel] += 1

            E -= E_loss
            if E < 0.01:
                break

            l, m, n = ray()

            x_entry, y_entry, z_entry = x_int, y_int, z_int

channels = np.arange(n_channels)
energies = E_min + channels * channel_width

plt.figure(figsize=(10, 6))
plt.bar(energies, spectrum, width=channel_width, align='edge')
plt.xlabel('Энергия (МэВ)')
plt.ylabel('Количество событий')
plt.title('Моделируемый спектр гамма-излучения от Cs-137 в детекторе NaI')
plt.grid(True)
plt.show()
