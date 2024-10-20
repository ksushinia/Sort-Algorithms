import numpy as np
import matplotlib.pyplot as plt

# Данные для отсортированного массива
sortedSize = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.001654, 0.000481, 0.000707, 0.000603, 0.000817, 0.001067, 0.001518, 0.001798, 0.002042, 0.002367, 0.002788, 0.002243, 0.002439, 0.001663, 0.003578])

# Параметры для графика
plt.figure(figsize=(12, 8))

# Подгонка полинома второго порядка
coeffs = np.polyfit(sortedSize, sorted_times, 2)
poly = np.poly1d(coeffs)

# Получение значений для регрессионной кривой
x_line = np.linspace(min(sortedSize), max(sortedSize), 100)
y_line = poly(x_line)

# Построение точек и регрессионной кривой
plt.scatter(sortedSize, sorted_times, label="Отсортированный (данные)", s=100)  # Точки
plt.plot(x_line, y_line, label="Отсортированный (регрессия)", linewidth=2)  # Регрессия

# Настройки графика
plt.title("Регрессионная кривая для времени сортировки (отсортированный массив) (Merge Sort)")
plt.xlabel("Размер массива")
plt.ylabel("Время (в секундах)")
plt.legend()
plt.grid()
plt.show()
