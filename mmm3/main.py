import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3 - 2*(x**2) - np.sin(x) + 1

X = np.arange(-1.5,2.5,0.1)
plt.plot(X, func(X))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


epsilon = 0.0001
left = float(input("Левая граница a: "))
right = float(input("Правая граница b: "))

if(not (func(left)*func(right) < 0)):
    print("неверно введен интервал (y(a)⋅y(b)<0)")
    exit()

while(right-left > epsilon):
    x0 = (left + right)/2
    if(func(left)*func(x0) < 0):
        right = x0
    else:
        left = x0
    if(right-left < epsilon):
        print("x0 =", x0)
        print("f(x0) =",func(x0))
