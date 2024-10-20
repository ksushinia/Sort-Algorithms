import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные размеров массивов
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных типов массивов (в секундах)
sorted_times = np.array([0.000507, 0.000889, 0.000360, 0.000104, 0.000151, 0.000201, 0.000152, 0.000222, 0.000244, 0.000285, 0.000242, 0.000244, 0.000408, 0.000402, 0.000496])
nearly_sorted_times = np.array([0.001103, 0.000623, 0.000585, 0.000539, 0.000797, 0.000984, 0.001204, 0.001291, 0.001427, 0.001782, 0.001699, 0.002104, 0.002288, 0.002720, 0.002634])
reverse_sorted_times = np.array([0.000672, 0.000482, 0.000386, 0.000121, 0.000221, 0.000264, 0.000300, 0.000296, 0.000324, 0.000364, 0.000468, 0.000479, 0.000387, 0.000522, 0.000656])
random_sorted_times = np.array([0.001167, 0.000618, 0.000601, 0.000612, 0.000947, 0.001131, 0.001268, 0.001625, 0.001607, 0.001699, 0.002050, 0.002344, 0.002489, 0.002992, 0.003020])

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
plt.title('Все случаи Hibbard Sort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()
plt.show()