import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для обратно отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
reverse_sorted_times = np.array([0.003918, 0.007531, 0.008435, 0.006026, 0.009468, 0.012633, 0.013754, 0.022828, 0.028758, 0.033073, 0.039767, 0.052808, 0.065667, 0.071347, 0.067165])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
reverse_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure()
plt.scatter(sizes, reverse_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для обратно отсортированного массива с регрессионной кривой (Insertion Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
