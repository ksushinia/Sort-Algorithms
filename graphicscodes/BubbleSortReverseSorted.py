import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для обратно отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
reverse_sorted_times = np.array([0.001395, 0.002874, 0.006379, 0.011276, 0.018086, 0.025717, 0.036099, 0.046457, 0.059484, 0.070787, 0.085972, 0.102689, 0.120641, 0.140430, 0.160319])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
reverse_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, reverse_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для обратно отсортированного массива с регрессионной кривой (Bubble Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
