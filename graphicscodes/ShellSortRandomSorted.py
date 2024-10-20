import matplotlib.pyplot as plt
import numpy as np

# Данные для случайно отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [
    0.001220, 0.000506, 0.000537, 0.000575, 0.000762,
    0.000948, 0.001313, 0.001711, 0.001609, 0.001704,
    0.001851, 0.002366, 0.002735, 0.003408, 0.003068
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
plt.title('Время выполнения Shell Sort (Случайно отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
