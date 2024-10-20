import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для случайно отсортированных массивов для разных сортировок
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных сортировок
random_times_merge = np.array([0.000389, 0.000665, 0.001065, 0.001275, 0.003023, 0.002331, 0.002670, 0.002473, 0.002558, 0.003592, 0.003262, 0.002911, 0.003123, 0.004482, 0.005371])
random_times_pratt = np.array([0.000691, 0.000741, 0.000752, 0.001519, 0.001486, 0.002354, 0.002342, 0.002653, 0.003239, 0.004087, 0.004018, 0.004155, 0.005871, 0.005172, 0.007292])
random_times_quick = np.array([0.000234, 0.000276, 0.000400, 0.000532, 0.000606, 0.001007, 0.000767, 0.000989, 0.001170, 0.001270, 0.001517, 0.001667, 0.001611, 0.002092, 0.002252])
random_times_heap = np.array([0.000405, 0.000505, 0.000970, 0.001105, 0.000752, 0.001191, 0.001696, 0.001337, 0.001755, 0.001624, 0.001746, 0.002009, 0.002066, 0.002227, 0.002667])

# Построение регрессионных кривых для каждой сортировки (полином степени 2)
p_merge = Polynomial.fit(sizes, random_times_merge, deg=2)
p_pratt = Polynomial.fit(sizes, random_times_pratt, deg=2)
p_quick = Polynomial.fit(sizes, random_times_quick, deg=2)
p_heap = Polynomial.fit(sizes, random_times_heap, deg=2)

# Для плавных кривых
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
merge_times_smooth = p_merge(sizes_smooth)
pratt_times_smooth = p_pratt(sizes_smooth)
quick_times_smooth = p_quick(sizes_smooth)
heap_times_smooth = p_heap(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))

# Построение регрессионных кривых
plt.plot(sizes_smooth, merge_times_smooth, label='Merge Sort', color='blue', linewidth=2)
plt.plot(sizes_smooth, pratt_times_smooth, label='Pratt Sort', color='green', linewidth=2)
plt.plot(sizes_smooth, quick_times_smooth, label='Quick Sort', color='red', linewidth=2)
plt.plot(sizes_smooth, heap_times_smooth, label='Heap Sort', color='purple', linewidth=2)

# Логарифмическая шкала для оси Y
plt.yscale('log')

# Настройка графика
plt.title('Сравнение времени выполнения различных сортировок с логарифмической шкалой')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True, which="both", ls="--")
plt.legend()

# Показать график
plt.show()
