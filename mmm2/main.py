import numpy as np
import time

def f(x, y, z):
    """Подынтегральная функция."""
    return x**2 + y**2 + z**2

def exact_integral():
    """Точное значение интеграла для f(x,y,z)=x^2+y^2+z^2 на [0,1]^3."""
    return 1.0  # ∫∫∫ (x^2+y^2+z^2) dx dy dz = 3 * ∫_0^1 x^2 dx = 3 * 1/3 = 1

def rectangle_method(N):
    """
    Метод прямоугольников для тройного интеграла.
    N - количество разбиений по каждой оси (шаг h = 1/N).
    """
    h = 1.0 / N
    total = 0.0
    for i in range(N):
        x = (i + 0.5) * h  # середина интервала по x
        for j in range(N):
            y = (j + 0.5) * h  # середина интервала по y
            for k in range(N):
                z = (k + 0.5) * h  # середина интервала по z
                total += f(x, y, z)
    volume = h**3
    return total * volume


def monte_carlo_mean_value(M, batch_size=10000):
    """
    Метод Монте-Карло выборочного среднего для тройного интеграла.
    M - общее количество случайных точек.
    batch_size - размер пакета для генерации точек (для эффективности памяти)
    """
    total_sum = 0.0
    batches = M // batch_size
    remainder = M % batch_size
    
    # Обработка полных пакетов
    for _ in range(batches):
        # Генерируем случайные точки в [0,1]^3
        points = np.random.rand(batch_size, 3)
        # Вычисляем значения функции в этих точках
        values = f(points[:, 0], points[:, 1], points[:, 2])
        total_sum += np.sum(values)
    
    # Обработка остатка
    if remainder > 0:
        points = np.random.rand(remainder, 3)
        values = f(points[:, 0], points[:, 1], points[:, 2])
        total_sum += np.sum(values)
    
    # Объем области интегрирования (для единичного куба = 1)
    volume = 1.0
    return (total_sum / M) * volume


def main():
    exact = exact_integral()
    print(f"Точное значение интеграла: {exact}\n")

    # Метод прямоугольников с разными шагами
    N_values = [10, 20, 50, 100]
    print("Метод прямоугольников:")
    print("N\tПриближённое\tПогрешность\tВремя (с)")
    for N in N_values:
        start = time.time()
        approx = rectangle_method(N)
        end = time.time()
        error = abs(approx - exact)
        print(f"{N}\t{approx:.6f}\t{error:.6f}\t{end-start:.4f}")

    # Метод Монте-Карло с разными выборками
    M_values = [1000, 10000, 100000, 1000000, 10000000]
    print("\nМетод Монте-Карло:")
    print("M\tПриближённое\tПогрешность\tВремя (с)")
    for M in M_values:
        start = time.time()
        approx = monte_carlo_mean_value(M)
        end = time.time()
        error = abs(approx - exact)
        print(f"{M}\t{approx:.6f}\t{error:.6f}\t{end-start:.4f}")

main()