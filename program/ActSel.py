from random import randint
import matplotlib.pyplot as plt

def plot_segments(s, co, k, coef):
    for i  in s:
        d = [k,k]
        plt.plot(i, d, color=co)
        k-=coef
    

def actsel(s):
    solution = []
    while len(s) > 0:
        m = min(x[1] for x in s)
        minindex = next(i for i in range(len(s)) if m == s[i][1])
        print(minindex)
        d = s[minindex]
        solution.append(d)
        i = 0
        while i < len(s):
            if  s[i][0]<=d[1]:
                s.pop(i)
            else:
                i += 1
    return solution


s = [[a, randint(a+1, 1100)] for a in (randint(0, 1000) for _ in range(10))]
plot_segments(s, "blue", 40, 10)
print(s)
sol = actsel(s)
print(sol)
plot_segments(sol, "red", 50, 0)
plt.xlabel('Номер отрезка')
plt.ylabel('Значение')
plt.show()