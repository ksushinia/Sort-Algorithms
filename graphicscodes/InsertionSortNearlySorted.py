import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для почти отсортированного массива
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
nearly_sorted_times = np.array([0.001476, 0.002350, 0.001367, 0.001791, 0.001219, 0.001538, 0.002201, 0.003416, 0.003259, 0.003673, 0.005304, 0.004887, 0.006061, 0.006144, 0.007104])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
nearly_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure()
plt.scatter(sizes, nearly_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для почти отсортированного массива с регрессионной кривой (Insertion Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
