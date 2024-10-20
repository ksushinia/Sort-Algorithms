import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных типов массивов
sorted_times = np.array([0.001654, 0.000481, 0.000707, 0.000603, 0.000817, 0.001067, 0.001518, 0.001798, 0.002042, 0.002367, 0.002788, 0.002243, 0.002439, 0.001663, 0.003578])
nearly_sorted_times = np.array([0.000416, 0.000558, 0.000888, 0.000848, 0.001270, 0.001531, 0.002033, 0.002186, 0.002356, 0.002837, 0.002823, 0.002553, 0.002938, 0.003266, 0.003915])
reverse_sorted_times = np.array([0.000295, 0.000480, 0.000731, 0.000770, 0.001207, 0.001174, 0.001717, 0.001870, 0.002231, 0.002151, 0.002179, 0.001983, 0.001826, 0.002543, 0.003084])
random_sorted_times = np.array([0.000389, 0.000665, 0.001065, 0.001275, 0.003023, 0.002331, 0.002670, 0.002473, 0.002558, 0.003592, 0.003262, 0.002911, 0.003123, 0.004482, 0.005371])

# Настройка графика
plt.figure(figsize=(12, 8))

# Регрессия для отсортированного массива
p_sorted = Polynomial.fit(sizes, sorted_times, deg=2)
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
sorted_times_smooth = p_sorted(sizes_smooth)
plt.plot(sizes_smooth, sorted_times_smooth, color='blue', label='Отсортированный массив', linewidth=2)

# Регрессия для почти отсортированного массива
p_nearly_sorted = Polynomial.fit(sizes, nearly_sorted_times, deg=2)
nearly_sorted_times_smooth = p_nearly_sorted(sizes_smooth)
plt.plot(sizes_smooth, nearly_sorted_times_smooth, color='orange', label='Почти отсортированный массив', linewidth=2)

# Регрессия для массива в обратном порядке
p_reverse_sorted = Polynomial.fit(sizes, reverse_sorted_times, deg=2)
reverse_sorted_times_smooth = p_reverse_sorted(sizes_smooth)
plt.plot(sizes_smooth, reverse_sorted_times_smooth, color='green', label='Массив в обратном порядке', linewidth=2)

# Регрессия для случайно отсортированного массива
p_random_sorted = Polynomial.fit(sizes, random_sorted_times, deg=2)
random_sorted_times_smooth = p_random_sorted(sizes_smooth)
plt.plot(sizes_smooth, random_sorted_times_smooth, color='red', label='Случайно отсортированный массив', linewidth=2)

# Настройки графика
plt.title('Все случаи Merge Sort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()
plt.show()
