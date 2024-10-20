import matplotlib.pyplot as plt
import numpy as np

# Данные для отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
sorted_times = [0.000283, 0.000405, 0.000190, 0.000216, 0.000252, 0.000245,
                0.000180, 0.000293, 0.000341, 0.000297, 0.000327, 0.000376,
                0.000358, 0.000379, 0.000448]

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
plt.title('Время выполнения сортировки Shell Sort (Отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
