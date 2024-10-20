import matplotlib.pyplot as plt
import numpy as np

# Данные для почти отсортированного массива (из таблицы QuickSort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [0.000345, 0.000234, 0.000248, 0.000327, 0.000390, 0.000492,
                       0.000581, 0.000606, 0.000621, 0.000727, 0.000698, 0.000843,
                       0.001043, 0.001129, 0.000938]

# Построение графика в формате точек
plt.scatter(sizes, nearly_sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, nearly_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения QuickSort (Почти отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
