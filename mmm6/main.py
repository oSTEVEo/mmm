import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
from scipy.integrate import solve_ivp

from integrate import solve, optimal_step

# Условие
intervals = ((0., 1.),
             (0., 5.),
             (0., 10.))
y0 = (0., 1.) # y(0)=0; y'(0)=1

def func(x, y):
    """f(x, y)=(f1, f2), где x - скаляр, y=(y1, y2) - вектор."""
    y1, y2 = y
    
    f1 = y2
    f2 = (x**2 - 1)*np.cos(3*x) - (x**2 + 1)*np.sin(3*x*y2) + (x+5)*np.sin(2*x*y1)
    return np.array([f1, f2])

def phaze_and_solve_graph(x_vals, y, y_prime):
    "Построение фазового портрета и решения"
    dot_alpha = 0.5
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(y, y_prime, 'b-', linewidth=1)
    plt.xlabel("y")
    plt.ylabel("y'")
    plt.title("Зависимость y(y')")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(x_vals, y, 'r-', label="y(x)", alpha=dot_alpha)
    plt.plot(x_vals, y_prime, 'g--', label="y'(x)")
    plt.xlabel("x")
    plt.ylabel("y, y'")
    plt.legend()
    plt.title("Решение y(x) и y'(x)")
    plt.grid(True)

    plt.tight_layout()
    T = x_vals[-1] - x_vals[0]
    plt.savefig(f"plots/phaze_and_solve_{T:.0f}.png")

def adams_vs_scipy_cmp_graph(x_vals, y, y_prime, x_ivp, y_ivp, y_prime_ivp):
    "Построение сравнения решения из scipy и решения методом Адамса"
    dot_alpha = 0.5
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(x_ivp, y_ivp, 'b-', linewidth=2, label='scipy')
    plt.plot(x_vals, y, 'ro', markersize=4, label='Метод Адамса y(x)', alpha=dot_alpha)
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(x_ivp, y_prime_ivp, 'b-', linewidth=2, label="scipy")
    plt.plot(x_vals, y_prime, 'ro', markersize=4, label="Метод Адамса y'(x)", alpha=dot_alpha)
    plt.xlabel('x')
    plt.ylabel("y'(x)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    T = x_vals[-1] - x_vals[0]
    plt.savefig(f"plots/adams_vs_scipy_cmp_{T:.0f}.png")

# Прогон для разных отрезков
for interval in intervals:
    print(f"Интервал: {interval}")
    # Решение Адамса
    h = optimal_step(func, interval, y0, eps=1e-4)
    print(f"Подобран оптимальный шаг: h = {h:.2e}")
    x_vals, y_vals = solve(func, interval, y0, h)
    y = y_vals[:, 0]
    y_prime = y_vals[:, 1]

    # Решение scipy
    sol_ivp = solve_ivp(func, interval, y0, method='LSODA', dense_output=True)
    x_ivp = np.linspace(interval[0], interval[1], 1000)
    y_ivp = sol_ivp.sol(x_ivp)[0]  # y(x)
    y_prime_ivp = sol_ivp.sol(x_ivp)[1]  # y'(x)

    # Построение графиков    
    phaze_and_solve_graph(x_vals, y, y_prime)
    adams_vs_scipy_cmp_graph(x_vals, y, y_prime, x_ivp, y_ivp, y_prime_ivp)
    
    # Печать значений
    print("x         y          y'")
    for i in range(0, len(x_vals), max(1, len(x_vals)//10)):
        print(f"{x_vals[i]:.4f}  {y[i]:.6f}  {y_prime[i]:.6f}")

    #sol = solve_ivp(func, interval, y0, method='LSODA')
    print("Решение в последней точке используя LSODA из scipy")
    print(f"x = {x_ivp[-1]:.2f}, y = {y_ivp[-1]:.6f}, y' = {y_prime_ivp[-1]:.6f}")    