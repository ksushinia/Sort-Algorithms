import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные размеров массивов и время выполнения для различных типов массивов (в секундах)
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000609, 0.000133, 0.000187, 0.000201, 0.000246,
                         0.000291, 0.000372, 0.000247, 0.000281, 0.000375,
                         0.000273, 0.000395, 0.000490, 0.000409, 0.000755])
nearly_sorted_times = np.array([0.000345, 0.000234, 0.000248, 0.000327, 0.000390,
                                0.000492, 0.000581, 0.000606, 0.000621, 0.000727,
                                0.000698, 0.000843, 0.001043, 0.001129, 0.000938])
reverse_sorted_times = np.array([0.000184, 0.000171, 0.000157, 0.000211, 0.000242,
                                 0.000306, 0.000354, 0.000295, 0.000230, 0.000378,
                                 0.000285, 0.000457, 0.000404, 0.000565, 0.000379])
random_sorted_times = np.array([0.000234, 0.000276, 0.000400, 0.000532, 0.000606,
                                0.001007, 0.000767, 0.000989, 0.001170, 0.001270,
                                0.001517, 0.001667, 0.001611, 0.002092, 0.002252])

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

# Регрессия для случайного массива
p_random_sorted = Polynomial.fit(sizes, random_sorted_times, deg=2)
random_sorted_times_smooth = p_random_sorted(sizes_smooth)
plt.plot(sizes_smooth, random_sorted_times_smooth, color='red', label='Случайно отсортированный массив', linewidth=2)

# Настройки графика
plt.title('Все случаи QuickSort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()
plt.show()
