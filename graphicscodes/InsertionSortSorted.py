import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.001654, 0.000481, 0.000707, 0.000603, 0.000817, 0.001067, 0.001518, 0.001798, 0.002042, 0.002367, 0.002788, 0.002243, 0.002439, 0.001663, 0.003578])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для отсортированного массива с регрессионной кривой (Insertion Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
