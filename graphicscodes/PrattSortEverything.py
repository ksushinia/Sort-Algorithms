import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные размеров массивов
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных типов массивов (в секундах)
sorted_times = np.array([0.003866, 0.000602, 0.000677, 0.000799, 0.000791, 0.001212, 0.001511, 0.001349, 0.002059, 0.001799, 0.002376, 0.002258, 0.003249, 0.002548, 0.002909])
nearly_sorted_times = np.array([0.002101, 0.000737, 0.000742, 0.001412, 0.001327, 0.001865, 0.002132, 0.002480, 0.003507, 0.003052, 0.003413, 0.003690, 0.005296, 0.004877, 0.005323])
reverse_sorted_times = np.array([0.001319, 0.000594, 0.000580, 0.000897, 0.000830, 0.001368, 0.001251, 0.001496, 0.002072, 0.001872, 0.002147, 0.002308, 0.003295, 0.002802, 0.004262])
random_sorted_times = np.array([0.000691, 0.000741, 0.000752, 0.001519, 0.001486, 0.002354, 0.002342, 0.002653, 0.003239, 0.004087, 0.004018, 0.004155, 0.005871, 0.005172, 0.007292])

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
plt.title('Все случаи Pratt Sort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()
plt.show()
