import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для почти отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
nearly_sorted_times = np.array([0.000416, 0.000558, 0.000888, 0.000848, 0.001270, 0.001531, 0.002033, 0.002186, 0.002356, 0.002837, 0.002823, 0.002553, 0.002938, 0.003266, 0.003915])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
nearly_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, nearly_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для почти отсортированного массива с регрессионной кривой (Bubble Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
