import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt


class HexahedronDetector:
    def __init__(self, vertices: List[np.ndarray]):
        self.vertices = np.array(vertices)
        # Разбиваем каждую из 6 граней гексаэдра на 2 треугольника
        self.triangles = []
        faces = [
            [0, 1, 2, 3],  # Нижняя грань
            [4, 5, 6, 7],  # Верхняя грань
            [0, 1, 5, 4],  # Передняя грань
            [1, 2, 6, 5],  # Правая грань
            [2, 3, 7, 6],  # Задняя грань
            [3, 0, 4, 7]  # Левая грань
        ]

        for face in faces:
            self.triangles.append((self.vertices[face[0]], self.vertices[face[1]], self.vertices[face[2]]))
            self.triangles.append((self.vertices[face[0]], self.vertices[face[2]], self.vertices[face[3]]))

    def ray_intersect(self, ray_origin: np.ndarray, ray_dir: np.ndarray) -> bool:
        for v0, v1, v2 in self.triangles:
            e1 = v1 - v0
            e2 = v2 - v0

            p = np.cross(ray_dir, e2)

            det = np.dot(e1, p)

            if abs(det) < 1e-6:
                continue

            inv_det = 1.0 / det
            tvec = ray_origin - v0

            u = np.dot(tvec, p) * inv_det
            if u < 0 or u > 1:
                continue

            q = np.cross(tvec, e1)

            v = np.dot(ray_dir, q) * inv_det
            if v < 0 or u + v > 1:
                continue

            t = np.dot(e2, q) * inv_det
            if t > 0:
                return True
        return False

class ParticleSource:
    def __init__(self, position: np.ndarray):
        self.position = np.array(position, dtype=float)

    def generate_particle(self) -> Tuple[np.ndarray, np.ndarray]:
        theta = np.arccos(2 * np.random.random() - 1)  # Полярный угол
        phi = 2 * np.pi * np.random.random()  # Азимутальный угол

        direction = np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta)
        ])
        return self.position, direction

def simulate(source_pos: np.ndarray, detector: HexahedronDetector, num_particles: int = 100000) -> float:
    source = ParticleSource(source_pos)
    hits = 0
    for _ in range(num_particles):
        origin, direction = source.generate_particle()
        if detector.ray_intersect(origin, direction):
            hits += 1
    return (hits / num_particles) * 100

def run_tests():
    cube_vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Нижняя грань
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]        # Верхняя грань
    ]
    detector = HexahedronDetector(cube_vertices)

    percentage = simulate([0, 0, 0], detector, 10000)
    print(f"Тест 1 (центр куба): {percentage:.2f}% (ожидается ~100%)")

    percentage = simulate([0, 0, 1], detector, 10000)
    print(f"Тест 2 (центр грани): {percentage:.2f}% (ожидается ~50%)")

    percentage = simulate([1, 0, 1], detector, 10000)
    print(f"Тест 3 (центр ребра): {percentage:.2f}% (ожидается ~25%)")

    percentage = simulate([1, 1, 1], detector, 10000)
    print(f"Тест 4 (вершина куба): {percentage:.2f}% (ожидается ~12.5%)")

if __name__ == "__main__":
    print("=== Тестирование для разных положений источника ===")
    run_tests()


def plot_distance_dependency():
    cube_vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Нижняя грань
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]  # Верхняя грань
    ]
    detector = HexahedronDetector(cube_vertices)
    distances = np.linspace(0, 10, 11)
    percentages = []
    for L in distances:
        percent = simulate([0, 0, L], detector, 5000)
        percentages.append(percent)

    plt.figure(figsize=(10, 6))
    plt.plot(distances, percentages, 'bo-', label='Моделирование')
    plt.xlabel('Расстояние до центра куба (L)')
    plt.ylabel('Процент попаданий (%)')
    plt.title('Зависимость процента попаданий от расстояния\n(Кубический детектор 2x2x2)')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    print("Исследование зависимости процента попаданий от расстояния")
    plot_distance_dependency()
