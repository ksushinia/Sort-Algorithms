import numpy as np
import matplotlib.pyplot as plt

# Данные для различных случаев
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.005574, 0.001740, 0.003732, 0.007686, 0.010974, 0.015535, 0.020217, 0.029127, 0.039143, 0.058127, 0.053653, 0.067040, 0.078331, 0.080945, 0.098994])
nearly_sorted_times = np.array([0.003758, 0.001683, 0.004076, 0.006604, 0.012671, 0.017417, 0.020815, 0.034332, 0.040633, 0.049340, 0.070586, 0.068291, 0.083345, 0.084548, 0.106999])
reverse_sorted_times = np.array([0.003254, 0.002362, 0.008363, 0.010273, 0.014550, 0.020489, 0.028249, 0.043195, 0.053185, 0.065987, 0.082097, 0.083822, 0.103148, 0.107793, 0.133518])
random_times = np.array([0.010060, 0.001824, 0.005714, 0.008467, 0.011079, 0.017326, 0.024610, 0.032152, 0.047880, 0.053028, 0.059921, 0.066272, 0.075475, 0.086703, 0.099986])

# Для интерполяции используем больше точек между исходными
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)

# Полиномиальная аппроксимация
sorted_smooth = np.poly1d(np.polyfit(sizes, sorted_times, 3))(sizes_smooth)
nearly_sorted_smooth = np.poly1d(np.polyfit(sizes, nearly_sorted_times, 3))(sizes_smooth)
reverse_sorted_smooth = np.poly1d(np.polyfit(sizes, reverse_sorted_times, 3))(sizes_smooth)
random_smooth = np.poly1d(np.polyfit(sizes, random_times, 3))(sizes_smooth)

# Построение графиков
plt.plot(sizes_smooth, sorted_smooth, label="Отсортированный массив", linewidth=2)
plt.plot(sizes_smooth, nearly_sorted_smooth, label="Частично отсортированный массив", linewidth=2)
plt.plot(sizes_smooth, reverse_sorted_smooth, label="Обратно отсортированный массив", linewidth=2)
plt.plot(sizes_smooth, random_smooth, label="Случайный массив", linewidth=2)

# Добавление точек из таблицы
plt.scatter(sizes, sorted_times, color='blue', marker='o', label='Отсортированный массив (данные)')
plt.scatter(sizes, nearly_sorted_times, color='orange', marker='o', label='Частично отсортированный массив (данные)')
plt.scatter(sizes, reverse_sorted_times, color='green', marker='o', label='Обратно отсортированный массив (данные)')
plt.scatter(sizes, random_times, color='red', marker='o', label='Случайный массив (данные)')

# Оформление графика
plt.title('Selection Sort - все случаи')
plt.xlabel('Размер массива')
plt.ylabel('Время (с)')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
