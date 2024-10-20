import numpy as np
import matplotlib.pyplot as plt

# Данные размеров массивов и времени выполнения для различных типов массивов (в секундах)
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000609, 0.000133, 0.000187, 0.000201, 0.000246, 0.000291, 0.000372, 0.000247, 0.000281, 0.000375, 0.000273, 0.000395, 0.000490, 0.000409, 0.000755])
nearly_sorted_times = np.array([0.000345, 0.000234, 0.000248, 0.000327, 0.000390, 0.000492, 0.000581, 0.000606, 0.000621, 0.000727, 0.000698, 0.000843, 0.001043, 0.001129, 0.000938])
reverse_sorted_times = np.array([0.000184, 0.000171, 0.000157, 0.000211, 0.000242, 0.000306, 0.000354, 0.000295, 0.000230, 0.000378, 0.000285, 0.000457, 0.000404, 0.000565, 0.000379])
random_times = np.array([0.000234, 0.000276, 0.000400, 0.000532, 0.000606, 0.001007, 0.000767, 0.000989, 0.001170, 0.001270, 0.001517, 0.001667, 0.001611, 0.002092, 0.002252])

# Параметры для графика
plt.figure(figsize=(12, 8))

# Функция для построения регрессионной кривой
def plot_regression(x, y, label):
    # Подгонка полинома второго порядка
    coeffs = np.polyfit(x, y, 2)
    poly = np.poly1d(coeffs)
    # Получение значений для регрессионной кривой
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)
    # Построение точек и регрессионной кривой
    plt.scatter(x, y, label=f"{label} (данные)", s=100)  # Точки
    plt.plot(x_line, y_line, label=f"{label} (кривая)", linewidth=2)  # Регрессия

# Построение для каждого типа массива
plot_regression(sizes, sorted_times, "Отсортированный")
plot_regression(sizes, nearly_sorted_times, "Почти отсортированный")
plot_regression(sizes, reverse_sorted_times, "Обратный отсортированный")
plot_regression(sizes, random_times, "Случайный")

# Настройки графика
plt.title("Все случаи Quick Sort с точками")
plt.xlabel("Размер массива")
plt.ylabel("Время выполнения (с)")
plt.legend()
plt.grid()
plt.show()
