import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для массива в обратном порядке
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
reverse_sorted_times = np.array([0.000295, 0.000480, 0.000731, 0.000770, 0.001207, 0.001174, 0.001717, 0.001870, 0.002231, 0.002151, 0.002179, 0.001983, 0.001826, 0.002543, 0.003084])

# Построение регрессионной кривой (многочлен степени 2)
p = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
reverse_sorted_times_smooth = p(sizes_smooth)

# Построение графика
plt.figure(figsize=(12, 8))
plt.scatter(sizes, reverse_sorted_times, color='blue', label='Точки')  # Точки
plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='red', label='Регрессионная кривая')  # Кривая

# Настройка графика
plt.title('Время выполнения для массива в обратном порядке с регрессионной кривой (Merge Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
