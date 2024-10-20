import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import numpy as np

# Данные для почти отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [0.003758, 0.001683, 0.004076, 0.006604, 0.012671, 0.017417, 0.020815, 0.034332,
                       0.040633, 0.049340, 0.070586, 0.068291, 0.083345, 0.084548, 0.106999]

# Построение графика в формате точек
plt.scatter(sizes, nearly_sorted_times, label="Данные", color='green')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, nearly_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Selection Sort (Почти отсортированный массив)')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
