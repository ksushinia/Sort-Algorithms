import matplotlib.pyplot as plt
import numpy as np

# Данные для случайного массива (из таблицы Heap Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [0.000405, 0.000505, 0.000970, 0.001105, 0.000752,
                       0.001191, 0.001696, 0.001337, 0.001755, 0.001624,
                       0.001746, 0.002009, 0.002066, 0.002227, 0.002667]

# Построение графика в формате точек
plt.scatter(sizes, random_sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, random_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Heap Sort (Случайный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
