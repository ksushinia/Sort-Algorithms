import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для случайно отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
random_sorted_times = np.array([0.001581, 0.002297, 0.002996, 0.003242, 0.004782, 0.006893, 0.009093, 0.009871, 0.012591, 0.015686, 0.017060, 0.022549, 0.028010, 0.029843, 0.040771])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, random_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
random_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure()
plt.scatter(sizes, random_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, random_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для случайно отсортированного массива с регрессионной кривой (Insertion Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
