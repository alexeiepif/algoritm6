from random import randint
import matplotlib.pyplot as plt


def plot_segments(s, sol, c1, c2, k, coef):
    plt.xlabel('Номер отрезка')
    plt.ylabel('Значение')
    for i in s:
        d1 = [k, k]
        plt.plot(i, d1, color=c1, linewidth=10, solid_capstyle='butt')
        k -= coef
    d2 = [50, 50]
    for k in range(len(sol)):
        plt.plot(sol[k], d2, color=c2, linewidth=10, solid_capstyle='butt')

def actsel1(s):
    solution = []
    while len(s) > 0:
        m = min(x[1] for x in s)
        minindex = next(i for i in range(len(s)) if m == s[i][1])
        d = s[minindex]
        solution.append(d)
        i = 0
        while i < len(s):
            if s[i][0] <= d[1]:
                s.pop(i)
            else:
                i += 1
    return solution


def actsel2(s):
    s.sort(key=lambda x: x[1])
    solution = [s[0]]
    for i in s:
        if i[0] > solution[-1][1]:
            solution.append(i)
    return solution


s = [[a, randint(a+1, 1100)] for a in (randint(0, 1000) for _ in range(20))]
cps = s.copy()

plt.figure(1)
print("Массив отрезков: ", s)
sol = actsel1(s)
s = cps.copy()
print("\nНепересекающиеся отрезки: ", sol)
plot_segments(s, sol, "blue", "red", 40, 10)

print("\n\t\t-------------------------\t\t\n")
s = cps.copy()
plt.figure(2)
sol = actsel2(s)
print("Массив сортированных отрезков: ", s)
print("\nНепересекающиеся сортированные отрезки: ", sol)
plot_segments(s, sol, "blue", "red", 40, 10)

plt.show()
