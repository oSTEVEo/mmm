import matplotlib.pyplot as plt
import numpy as np

## Константы
num_bins = 50

## Входные данные
np.random.seed(42)
N = 50000
array = list(np.random.normal(0, 1, N))

## График функции дифференциального распределения 
plt.subplot(211)
counts, bin_edges = np.histogram(array, bins=num_bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
plt.plot(bin_centers, counts, "--")

## График функции интегрального распределения 
plt.subplot(212)
sorted_arr = np.sort(array)
n = len(sorted_arr)
y = np.arange(1, n+1) / n
plt.plot(sorted_arr, y)

# Show th graph
plt.show()