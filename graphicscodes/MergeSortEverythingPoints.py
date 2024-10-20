import numpy as np
import matplotlib.pyplot as plt

# Данные
sortedSize = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.001654, 0.000481, 0.000707, 0.000603, 0.000817, 0.001067, 0.001518, 0.001798, 0.002042, 0.002367, 0.002788, 0.002243, 0.002439, 0.001663, 0.003578])
nearly_sorted_times = np.array([0.000416, 0.000558, 0.000888, 0.000848, 0.001270, 0.001531, 0.002033, 0.002186, 0.003356, 0.002837, 0.002823, 0.002153, 0.002238, 0.003266, 0.003715])
reverse_sorted_times = np.array([0.000295, 0.000480, 0.000731, 0.000770, 0.001207, 0.001174, 0.001717, 0.001970, 0.002431, 0.002251, 0.002179, 0.001783, 0.001526, 0.002543, 0.002884])
random_times = np.array([0.000389, 0.000665, 0.001065, 0.001275, 0.003023, 0.002331, 0.002670, 0.002473, 0.002558, 0.003592, 0.003262, 0.002911, 0.003123, 0.004482, 0.005371])

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
plot_regression(sortedSize, sorted_times, "Отсортированный")
plot_regression(sortedSize, nearly_sorted_times, "Почти отсортированный")
plot_regression(sortedSize, reverse_sorted_times, "Обратный отсортированный")
plot_regression(sortedSize, random_times, "Случайный")

# Настройки графика
plt.title("Merge Sort все случаи с точками")
plt.xlabel("Размер массива")
plt.ylabel("Время (в секундах)")
plt.legend()
plt.grid()
plt.show()
