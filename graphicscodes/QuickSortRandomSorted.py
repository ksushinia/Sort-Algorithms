import matplotlib.pyplot as plt
import numpy as np

# Данные для случайного массива (из таблицы QuickSort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [0.000234, 0.000276, 0.000400, 0.000532, 0.000606, 0.001007,
                       0.000767, 0.000989, 0.001170, 0.001270, 0.001517, 0.001667,
                       0.001611, 0.002092, 0.002252]

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
plt.title('Время выполнения QuickSort (Случайный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
