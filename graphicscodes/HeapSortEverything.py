import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные размеров массивов и время выполнения для различных типов массивов (в секундах)
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.001519, 0.000439, 0.000698, 0.000885, 0.001219,
                         0.000943, 0.001071, 0.001421, 0.001628, 0.001273,
                         0.001563, 0.001267, 0.001366, 0.001480, 0.001625])
nearly_sorted_times = np.array([0.000390, 0.000458, 0.000855, 0.001189, 0.000809,
                                0.000781, 0.001150, 0.001570, 0.001710, 0.001407,
                                0.001561, 0.001444, 0.001587, 0.002139, 0.001877])
reverse_sorted_times = np.array([0.000367, 0.000436, 0.000715, 0.001039, 0.000583,
                                 0.000683, 0.001261, 0.001295, 0.001243, 0.001291,
                                 0.001261, 0.001754, 0.001450, 0.001560, 0.002153])
random_sorted_times = np.array([0.000405, 0.000505, 0.000970, 0.001105, 0.000752,
                                0.001191, 0.001696, 0.001337, 0.001755, 0.001624,
                                0.001746, 0.002009, 0.002066, 0.002227, 0.002667])

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
plt.title('Время выполнения Heap Sort для различных типов массивов')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()
plt.show()
