import matplotlib.pyplot as plt
import numpy as np

# Данные для случайно отсортированного массива (из таблицы Pratt Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [
    0.000691, 0.000741, 0.000752, 0.001519, 0.001486,
    0.002354, 0.002342, 0.002653, 0.003239, 0.004087,
    0.004018, 0.004155, 0.005871, 0.005172, 0.007292
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
plt.title('Время выполнения Pratt Sort (Случайно отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
