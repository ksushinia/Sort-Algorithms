import matplotlib.pyplot as plt
import numpy as np

# Данные для отсортированного массива (из таблицы Pratt Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
sorted_times = [0.003866, 0.000602, 0.000677, 0.000799, 0.000791, 0.001212,
                0.001511, 0.001349, 0.002059, 0.001799, 0.002376, 0.002258,
                0.003249, 0.002548, 0.002909]

# Построение графика в формате точек
plt.scatter(sizes, sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Pratt Sort (Отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
