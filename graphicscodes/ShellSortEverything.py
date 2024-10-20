import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные размеров массивов
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных типов массивов (в секундах)
sorted_times = np.array([0.000283, 0.000405, 0.000190, 0.000216, 0.000252, 0.000245, 0.000180, 0.000293, 0.000341, 0.000297, 0.000327, 0.000376, 0.000358, 0.000379, 0.000448])
nearly_sorted_times = np.array([0.001089, 0.000526, 0.000607, 0.000593, 0.000948, 0.000859, 0.001214, 0.001198, 0.001411, 0.001645, 0.001989, 0.002029, 0.002215, 0.002560, 0.002765])
reverse_sorted_times = np.array([0.000735, 0.000325, 0.000252, 0.000211, 0.000144, 0.000243, 0.000408, 0.000317, 0.000484, 0.000329, 0.000464, 0.000610, 0.000521, 0.000785, 0.000756])
random_sorted_times = np.array([0.001220, 0.000506, 0.000537, 0.000575, 0.000762, 0.000948, 0.001313, 0.001711, 0.001609, 0.001704, 0.001851, 0.002366, 0.002735, 0.003408, 0.003068])

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
plt.title('Все случаи Shell Sort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (в секундах)')
plt.grid(True)
plt.legend()
plt.show()
