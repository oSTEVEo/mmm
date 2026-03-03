import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**2 - 4*np.sin(x) - 1

X = np.arange(-10,10,0.1)
plt.plot(X, func(X))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


epsilon = 0.0001
#тут вводим на глазок
left = float(input("Левая граница a: "))
right = float(input("Правая граница b: "))

if(not (func(left)*func(right) < 0)):
    print("неверно введен интервал (y(a)⋅y(b)<0)")
    exit()

while(right-left > epsilon):
    x1 = (left + right)/2
    if(func(left)*func(x1) < 0):
        right = x1
    else:
        left = x1
    if(right-left < epsilon):
        print("x1 =", x1)
        print("f(x1) =",func(x1))
