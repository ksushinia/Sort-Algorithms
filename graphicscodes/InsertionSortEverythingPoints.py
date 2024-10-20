import numpy as np
import matplotlib.pyplot as plt

# Данные для различных случаев
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000018, 0.000024, 0.000021, 0.000027, 0.000033, 0.000026, 0.000034, 0.000028, 0.000031, 0.000039, 0.000038, 0.000045, 0.000041, 0.000056, 0.000049])
nearly_sorted_times = np.array([0.001476, 0.002350, 0.001367, 0.001791, 0.001219, 0.001538, 0.002201, 0.003416, 0.003259, 0.003673, 0.005304, 0.004887, 0.006061, 0.006144, 0.007104])
reverse_sorted_times = np.array([0.003918, 0.007531, 0.008435, 0.006026, 0.009468, 0.012633, 0.013754, 0.022828, 0.028758, 0.033073, 0.039767, 0.052808, 0.065667, 0.071347, 0.067165])
random_times = np.array([0.001581, 0.002297, 0.002996, 0.003242, 0.004782, 0.006893, 0.009093, 0.009871, 0.012591, 0.015686, 0.017060, 0.022549, 0.028010, 0.029843, 0.040771])

# Для интерполяции используем больше точек между исходными
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)

# Полиномиальная аппроксимация
sorted_smooth = np.poly1d(np.polyfit(sizes, sorted_times, 3))(sizes_smooth)
nearly_sorted_smooth = np.poly1d(np.polyfit(sizes, nearly_sorted_times, 3))(sizes_smooth)
reverse_sorted_smooth = np.poly1d(np.polyfit(sizes, reverse_sorted_times, 3))(sizes_smooth)
random_smooth = np.poly1d(np.polyfit(sizes, random_times, 3))(sizes_smooth)

# Построение графиков
plt.plot(sizes_smooth, sorted_smooth, label="Отсортированный массив", linewidth=2)
plt.plot(sizes_smooth, nearly_sorted_smooth, label="Частично тсортированный массив", linewidth=2)
plt.plot(sizes_smooth, reverse_sorted_smooth, label="Обратно отсортированный массив", linewidth=2)
plt.plot(sizes_smooth, random_smooth, label="Случайный массив", linewidth=2)

# Добавление точек на график
plt.scatter(sizes, sorted_times, color='blue', label='Отсортированный массив (данные)', marker='o')
plt.scatter(sizes, nearly_sorted_times, color='orange', label='Частично тсортированный массив (данные)', marker='o')
plt.scatter(sizes, reverse_sorted_times, color='green', label='Обратно отсортированный массив (данные)', marker='o')
plt.scatter(sizes, random_times, color='red', label='Случайный массив (данные)', marker='o')

# Оформление графика
plt.title('Insertion Sort - все случаи с точками')
plt.xlabel('Размер массива')
plt.ylabel('Время (с)')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
