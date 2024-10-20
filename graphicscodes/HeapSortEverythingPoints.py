import numpy as np
import matplotlib.pyplot as plt

# Данные размеров массивов и времени выполнения для различных типов массивов (в секундах)
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.001519, 0.000439, 0.000698, 0.000885, 0.001219, 0.000943, 0.001071, 0.001421, 0.001628, 0.001273, 0.001563, 0.001267, 0.001366, 0.001480, 0.001625])
nearly_sorted_times = np.array([0.000390, 0.000458, 0.000855, 0.001189, 0.000809, 0.000781, 0.001150, 0.001570, 0.001710, 0.001407, 0.001561, 0.001444, 0.001587, 0.002139, 0.001877])
reverse_sorted_times = np.array([0.000367, 0.000436, 0.000715, 0.001039, 0.000583, 0.000683, 0.001261, 0.001295, 0.001243, 0.001291, 0.001261, 0.001754, 0.001450, 0.001560, 0.002153])
random_times = np.array([0.000405, 0.000505, 0.000970, 0.001105, 0.000752, 0.001191, 0.001696, 0.001337, 0.001755, 0.001624, 0.001746, 0.002009, 0.002066, 0.002227, 0.002667])

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
plt.title("Все случаи Heap Sort с точками")
plt.xlabel("Размер массива")
plt.ylabel("Время выполнения (с)")
plt.legend()
plt.grid()
plt.show()
