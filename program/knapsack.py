import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[2], reverse=True)
    solution_mas = {}
    solution_money = 0
    total_weight = 0

    for item in items:
        t = capacity - total_weight
        if (t) / item[2] > 1:
            solution_mas[item[0]] = item[2]
            total_weight += item[2]
            solution_money += item[1]
        else:
            solution_mas[item[0]] = t
            solution_money += item[1]/item[2]*t
            break

    return solution_mas, solution_money


n = 10
items_mas = [[i, random.randint(1, 100), random.randint(3, 20)]
             for i in range(n)]

print("Матрица:")
print(np.matrix(items_mas))

capacity = 30

solution, money = fractional_knapsack(items_mas, capacity)

print("\nРешение:")
for item in solution:
    print("Элемент", item, "был взят весом", solution[item])
print("Стоимость рюкзака = ", money)
fig, ax = plt.subplots()

ax.add_patch(patches.Rectangle((0, -0.5), capacity, 1, facecolor='gray'))

k = 0
y = 0.5

for i, value, weight in items_mas:
    if i in solution:
        ax.add_patch(patches.Rectangle((k, y), weight, 1))
        ax.text(k + weight / 2, 1, str(value),
                verticalalignment='center',
                horizontalalignment='center')
        if solution[i] == weight:
            ax.text(k + weight / 2, -0.5, str(solution[i]),
                    verticalalignment='top',
                    horizontalalignment='center')
            ax.text(k + weight / 2, 0, str(value),
                    verticalalignment='center',
                    horizontalalignment='center')
        else:
            ax.text((capacity + k)/2, -0.5, str(solution[i]),
                    verticalalignment='top',
                    horizontalalignment='center')
            ax.text((capacity + k)/2, 0, f"{value/weight* solution[i]:.2f}",
                    verticalalignment='center',
                    horizontalalignment='center')

        ax.text(k + weight / 2, 2, str(i),
                verticalalignment='bottom',
                horizontalalignment='center')
        ax.text(k + weight / 2, 1.5, str(weight),
                verticalalignment='bottom',
                horizontalalignment='center')
        if k > 0:  # не

            ax.axvline(x=k, ymin=0, ymax=2, color='red')
        k += weight


ax.text(-10, 2, "Элементы",
        verticalalignment='bottom',
        horizontalalignment='center')
ax.text(-10, 1.5, "Вес",
        verticalalignment='bottom',
        horizontalalignment='center')
ax.text(-10, 1, "Цена",
        verticalalignment='center',
        horizontalalignment='center')
ax.text(-10, 0, "Цена в рюкзаке",
        verticalalignment='center',
        horizontalalignment='center')
ax.text(-10, -0.5, "Вес в рюкзаке",
        verticalalignment='top',
        horizontalalignment='center')
plt.xlim(-8, k)
plt.ylim(-1, 2)

ax.axis('off')

plt.show()
