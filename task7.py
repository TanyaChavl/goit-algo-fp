import numpy as np
import matplotlib.pyplot as plt

# Кількість кидків
n_rolls = 1000000

# Генерація випадкових чисел для двох кубиків
rolls_1 = np.random.randint(1, 7, n_rolls)
rolls_2 = np.random.randint(1, 7, n_rolls)

# Обчислення сум для кожного кидка
sums = rolls_1 + rolls_2

# Підрахунок кількості кожної суми
sum_counts = np.bincount(sums)[2:]  # [2:] тому що мінімальна сума = 2

# Обчислення ймовірності кожної суми
probabilities = sum_counts / n_rolls

# Виведення результатів
for sum_value, probability in enumerate(probabilities, start=2):
    print(f"Сума: {sum_value}, Ймовірність: {probability*100:.2f}%")

# Графік
plt.figure(figsize=(10, 6))
plt.bar(range(2, 13), probabilities, tick_label=range(2, 13), color='skyblue')
plt.title('Ймовірність суми двох кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.grid(axis='y')

# Виведення графіка
plt.show()
