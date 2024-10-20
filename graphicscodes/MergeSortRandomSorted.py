import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для случайно отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
random_sorted_times = np.array([0.000389, 0.000665, 0.001065, 0.001275, 0.003023, 0.002331, 0.002670, 0.002473, 0.002558, 0.003592, 0.003262, 0.002911, 0.003123, 0.004482, 0.005371])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, random_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
random_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, random_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, random_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для случайно отсортированного массива с регрессионной кривой (Merge Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
