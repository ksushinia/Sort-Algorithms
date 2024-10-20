import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для различных случаев
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000037, 0.000004, 0.000004, 0.000003, 0.000004, 0.000003, 0.000004, 0.000005, 0.000006, 0.000007, 0.000004, 0.000005, 0.000013, 0.000006, 0.000005])
nearly_sorted_times = np.array([0.004004, 0.001354, 0.002065, 0.003720, 0.006047, 0.009006, 0.013248, 0.017047, 0.021540, 0.028174, 0.030484, 0.037728, 0.045543, 0.056539, 0.071851])
reverse_sorted_times = np.array([0.001395, 0.002874, 0.006379, 0.011276, 0.018086, 0.025717, 0.036099, 0.046457, 0.059484, 0.070787, 0.085972, 0.102689, 0.120641, 0.140430, 0.160319])
random_times = np.array([0.001794, 0.005107, 0.004717, 0.009298, 0.013376, 0.022216, 0.028064, 0.048378, 0.060630, 0.082880, 0.110587, 0.128625, 0.175136, 0.205286, 0.231990])

# Построение регрессионной кривой (многочлен степени 2)
p_sorted = Polynomial.fit(sizes, sorted_times, deg=2)
p_nearly_sorted = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
p_reverse_sorted = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
p_random = Polynomial.fit(sizes, random_times, deg=2)

sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)

# Получение значений для гладкой линии
sorted_times_smooth = p_sorted(sizes_smooth)
nearly_sorted_times_smooth = p_nearly_sorted(sizes_smooth)
reverse_sorted_times_smooth = p_reverse_sorted(sizes_smooth)
random_times_smooth = p_random(sizes_smooth)

# Построение графиков
plt.figure(figsize=(12, 8))

plt.scatter(sizes, sorted_times, color='blue', label='Отсортированный массив', zorder=5)  # Точки для отсортированного
plt.plot(sizes_smooth, sorted_times_smooth, color='blue', linestyle='-', linewidth=2, label='Кривая (отсортированный)')

plt.scatter(sizes, nearly_sorted_times, color='green', label='Частично отсортированный массив', zorder=5)  # Точки для почти отсортированного
plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='green', linestyle='-', linewidth=2, label='Кривая (частично отсортированный)')

plt.scatter(sizes, reverse_sorted_times, color='red', label='Обратно отсортированный массив', zorder=5)  # Точки для обратно отсортированного
plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='red', linestyle='-', linewidth=2, label='Кривая (обратно отсортированный)')

plt.scatter(sizes, random_times, color='orange', label='Случайный массив', zorder=5)  # Точки для случайного
plt.plot(sizes_smooth, random_times_smooth, color='orange', linestyle='-', linewidth=2, label='Кривая (случайный)')

# Настройка графика
plt.title('Bubble Sort все случаи с точками')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
