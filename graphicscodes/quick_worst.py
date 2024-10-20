import matplotlib.pyplot as plt
import numpy as np

# Размеры массивов
sizes = np.arange(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценка времени выполнения для худшего случая
worst_case = sizes ** 2  # O(n^2)

# Построение графика
plt.figure()

# График для худшего случая
plt.plot(sizes, worst_case, label='Худший случай O(n^2)', color='red')

# Оформление графика
plt.title('Асимптотическая сложность QuickSort (Худший случай O(n^2))')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
