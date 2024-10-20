import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для случайно отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
random_times = np.array([0.001794, 0.005107, 0.004717, 0.009298, 0.013376, 0.022216, 0.028064, 0.048378, 0.060630, 0.082880, 0.110587, 0.128625, 0.175136, 0.205286, 0.231990])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, random_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
random_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, random_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, random_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для случайно отсортированного массива с регрессионной кривой (Bubble Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
