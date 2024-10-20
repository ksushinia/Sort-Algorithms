import matplotlib.pyplot as plt
import numpy as np

# Данные для почти отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [
    0.001089, 0.000526, 0.000607, 0.000593, 0.000948,
    0.000859, 0.001214, 0.001198, 0.001411, 0.001645,
    0.001989, 0.002029, 0.002215, 0.002560, 0.002765
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
plt.title('Время выполнения сортировки Shell Sort (Почти отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
