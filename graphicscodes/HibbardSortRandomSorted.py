import matplotlib.pyplot as plt
import numpy as np

# Данные для случайно отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [
    0.001167, 0.000618, 0.000601, 0.000612, 0.000947,
    0.001131, 0.001268, 0.001625, 0.001607, 0.001699,
    0.002050, 0.002344, 0.002489, 0.002992, 0.003020
]

# Построение графика в формате точек
plt.scatter(sizes, random_sorted_times, label="Данные", color='green')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, random_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Hibbard Sort (Случайно отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
