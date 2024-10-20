import matplotlib.pyplot as plt
import numpy as np

# Данные для отсортированного массива (из таблицы QuickSort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
sorted_times = [0.000609, 0.000133, 0.000187, 0.000201, 0.000246, 0.000291,
                0.000372, 0.000247, 0.000281, 0.000375, 0.000273, 0.000395,
                0.000490, 0.000409, 0.000755]

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
plt.title('Время выполнения QuickSort (Отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
