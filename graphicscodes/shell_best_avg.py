import matplotlib.pyplot as plt
import numpy as np

# Размеры массивов
sizes = np.arange(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценки времени выполнения для случаев
best_case = sizes * np.log(sizes)        # O(n log n)
average_case = sizes ** (3/2)            # O(n^(3/2))

# Построение графика
plt.figure()

# График для лучшего случая
plt.plot(sizes, best_case, label='Лучший случай O(n log n)', color='green')
# График для среднего случая
plt.plot(sizes, average_case, label='Средний случай O(n^{3/2})', color='orange')

# Оформление графика
plt.title('Асимптотическая сложность сортировки Шелла')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
