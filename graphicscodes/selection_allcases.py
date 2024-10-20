import matplotlib.pyplot as plt

# Размеры массивов
sizes = range(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценки времени выполнения для лучшего, среднего и худшего случаев
best_case = [n**2 for n in sizes]        # O(n^2)
average_case = [n**2 for n in sizes]    # O(n^2)
worst_case = [n**2 for n in sizes]      # O(n^2)

# Построение графика
plt.figure()
plt.plot(sizes, best_case, label='Лучший случай O(n^2)', color='blue')
plt.plot(sizes, average_case, label='Средний случай O(n^2)', color='green')
plt.plot(sizes, worst_case, label='Худший случай O(n^2)', color='red')

# Оформление графика
plt.title('Асимптотическая сложность сортировки выбором')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
