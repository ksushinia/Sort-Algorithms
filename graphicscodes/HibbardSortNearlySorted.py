import matplotlib.pyplot as plt
import numpy as np

# Данные для почти отсортированного массива (из таблицы)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [
    0.001103, 0.000623, 0.000585, 0.000539, 0.000797,
    0.000984, 0.001204, 0.001291, 0.001427, 0.001782,
    0.001699, 0.002104, 0.002288, 0.002720, 0.002634
]

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
plt.title('Время выполнения сортировки Хиббарда (Почти отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
