import matplotlib.pyplot as plt
import numpy as np

# Размеры массивов
sizes = np.arange(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценки времени выполнения для лучшего случая
best_case = sizes  # O(n)

# Построение графика
plt.figure()

# График для лучшего случая
plt.plot(sizes, best_case, label='Лучший случай O(n)', color='green')

# Оформление графика
plt.title('Асимптотическая сложность сортировки пузырьком (Bubble Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
