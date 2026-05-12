import numpy as np
import matplotlib.pyplot as plt

n = 40
alpha, beta, gamma = 3, 1, 2
h = 1.0 / n
eps = h**3
N = n - 1 # число внутренних узлов (уравнений)

x = np.linspace(0, 1, n+1)
xi = x[1:-1] # внутренние узлы

def p(x): return 1 + x**gamma
def q(x): return x + 1
def u_exact(x): return x**alpha * (1-x)**beta
def f(x):
    return -x**5 + 20*x**4 - 11*x**3 + 12*x**2 - 6*x

p_vals = p(x)
q_vals = q(xi)
f_vals = f(xi)
# Диагонали трёхдиагональной матрицы
main_diag = p_vals[1:-1] + p_vals[2:] + h**2 * q_vals    # d_i
lower_diag = -p_vals[1:-1]                               # l_i (i=2..N)
upper_diag = -p_vals[2:]                                 # u_i (i=1..N-1)
rhs = f_vals * h**2                                      # b_i

print("Проверка устойчивости прогонки")
# Условие диагонального преобладания (строгое)
# Для первой и последней строки проверяем вручную
strict_first = abs(main_diag[0]) > abs(upper_diag[0])
strict_last  = abs(main_diag[-1]) > abs(lower_diag[-1])
strict_mid   = all(abs(main_diag[i]) > abs(lower_diag[i]) + abs(upper_diag[i]) for i in range(1, N-1))
print(f"Строгое диагональное преобладание в 1-й строке: {strict_first}")
print(f"Строгое диагональное преобладание в последней строке: {strict_last}")
print(f"Строгое диагональное преобладание в средних строках: {strict_mid}")
if strict_first and strict_last and strict_mid:
    print("Прогонка устойчива (достаточное условие выполнено).")
else:
    print("Внимание: условие строгого диагонального преобладания нарушено, но прогонка может быть ещё устойчива.")


# Метод прогонки (точное решение)
def classic_solve(d, l, u, b):
    n_eq = len(d)
    P = np.zeros(n_eq)
    Q = np.zeros(n_eq)
    P[0] = u[0] / d[0]
    Q[0] = b[0] / d[0]
    for i in range(1, n_eq-1):
        denom = d[i] - l[i] * P[i-1]
        P[i] = u[i] / denom
        Q[i] = (b[i] - l[i] * Q[i-1]) / denom
    i = n_eq - 1
    denom = d[i] - l[i] * P[i-1]
    Q[i] = (b[i] - l[i] * Q[i-1]) / denom
    y = np.zeros(n_eq)
    y[-1] = Q[-1]
    for i in range(n_eq-2, -1, -1):
        y[i] = Q[i] - P[i] * y[i+1]
    return y

y_thomas = classic_solve(main_diag, lower_diag, upper_diag, rhs)

# Метод наискорейшего спуска
def residual(y):
    """Вычисляет вектор невязки r = b - A y"""
    r = np.empty(N)
    r[0] = rhs[0] - (main_diag[0]*y[0] + upper_diag[0]*y[1])
    for i in range(1, N-1):
        r[i] = rhs[i] - (lower_diag[i]*y[i-1] + main_diag[i]*y[i] + upper_diag[i]*y[i+1])
    r[-1] = rhs[-1] - (lower_diag[-1]*y[-2] + main_diag[-1]*y[-1])
    return r

def A_mult(v):
    """Умножение матрицы A на вектор v"""
    Av = np.empty(N)
    Av[0] = main_diag[0]*v[0] + upper_diag[0]*v[1]
    for i in range(1, N-1):
        Av[i] = lower_diag[i]*v[i-1] + main_diag[i]*v[i] + upper_diag[i]*v[i+1]
    Av[-1] = lower_diag[-1]*v[-2] + main_diag[-1]*v[-1]
    return Av

def max_error(y_num):
    return np.max(np.abs(y_num - y_thomas))

y0 = np.zeros(N)
y_sd = y0.copy()
errors = []
max_iter = 50000
for it in range(max_iter):
    r = residual(y_sd)
    if np.max(np.abs(r)) <= eps:
        break
    Ar = A_mult(r)
    alpha = np.dot(r, r) / np.dot(r, Ar)
    y_sd = y_sd + alpha * r
    errors.append(max_error(y_sd))

it_sd = it + 1
print(f"\nМетод наискорейшего спуска: сошёлся за {it_sd} итераций.")
print(f"Максимальная невязка: {np.max(np.abs(residual(y_sd))):.2e}")


print("\nТаблица значений y_i (каждый 5-й узел):")
print(f"{'i':>3} {'x':>8} {'y_прогонка':>15} {'y_спуск':>15}")
step = 5
for idx in range(0, N, step):
    print(f"{idx+1:3d} {xi[idx]:8.4f} {y_thomas[idx]:15.10f} {y_sd[idx]:15.10f}")


# Решения
plt.figure(figsize=(10, 5))
plt.plot(xi, y_thomas, 'k-', linewidth=2, label='Прогонка (точное решение СЛАУ)')
plt.plot(xi, y_sd, 'r--', label=f'Наискорейший спуск ({it_sd} ит.)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Убывание погрешности max|y_k - y_thomas|
plt.figure(figsize=(10, 5))
plt.semilogy(range(1, len(errors)+1), errors, 'b-')
plt.xlabel('Номер итерации')
plt.ylabel('max|y_k - y_прогонки|')
plt.title('Сходимость метода наискорейшего спуска')
plt.grid(True)
plt.show()