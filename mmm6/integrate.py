import typing
import numpy as np

def runge_kutta4(f, x, y, h):
    """ Выполняет один шаг классического метода Рунге-Кутты 4-го порядка
    """
    k1 = f(x, y)
    k2 = f(x + h/2, y + h/2 * k1)
    k3 = f(x + h/2, y + h/2 * k2)
    k4 = f(x + h, y + h * k3)
    return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def optimal_step(func, interval, y0, eps=1e-6):
    for i in range(1, 101):
        h = 0.1 / i
        x1, U1 = solve(func, interval, y0, h)
        x2, U2 = solve(func, interval, y0, h/2)
        U2_new = U2[::2]
        if abs(U2_new[-1][0] - U1[-1][0]) < eps:
            optimal_h = h
            return optimal_h
    
    print("Не удалось подобрать шаг за 100 итераций")
    return 0.001

def solve(func: typing.Callable, interval, y0, x_step):
    """
    func - функция для решения
    interval - (x_start, x_end)
    y0 = (y(0); y'(0))
    """
    n_steps = int((interval[1] - interval[0]) / x_step)

    #Массивы для хранения решений
    x_vals, y_vals, f_vals = array_prepare(func, interval, y0, n_steps)

    #Первые 4 точки методом Рунге-Кутты
    for i in range(3):
        x_vals[i+1] = x_vals[i] + x_step
        y_vals[i+1] = runge_kutta4(func, x_vals[i], y_vals[i], x_step)
        f_vals[i+1] = func(x_vals[i+1], y_vals[i+1])

    for i in range(3, n_steps):
        #Предиктор и корректор
        f_pred = adams_bashfor(func, x_step, x_vals, y_vals, f_vals, i)
        y_next, f_next = adams_multon(func, x_step, x_vals, y_vals, f_vals, i, f_pred)

        x_vals[i+1] = x_vals[i] + x_step
        y_vals[i+1] = y_next
        f_vals[i+1] = f_next

    return x_vals, y_vals

def array_prepare(func, interval, y0, n_steps):
    x_vals = np.zeros(n_steps + 1)
    y_vals = np.zeros((n_steps + 1, 2))
    f_vals = np.zeros((n_steps + 1, 2))
    x_vals[0] = interval[0]
    y_vals[0] = y0
    f_vals[0] = func(interval[0], y0)
    return x_vals,y_vals,f_vals

def adams_multon(func, x_step, x_vals, y_vals, f_vals, i, f_pred):
    y_next = y_vals[i] + x_step/24 * (9*f_pred + 19*f_vals[i] - 5*f_vals[i-1] + f_vals[i-2])
    f_next = func(x_vals[i] + x_step, y_next)
    return y_next,f_next

def adams_bashfor(func, x_step, x_vals, y_vals, f_vals, i):
    y_pred = y_vals[i] + x_step/24 * (55*f_vals[i] - 59*f_vals[i-1] + 37*f_vals[i-2] - 9*f_vals[i-3])
    f_pred = func(x_vals[i] + x_step, y_pred)
    return f_pred
