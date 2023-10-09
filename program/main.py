import random as rnd


def pointscover1(s):
    segment = []
    while (len(s) > 0):
        xm = min(s)
        segment.append([xm, xm+1])
        i = 0
        while i < len(s):
            if segment[-1][0] <= s[i] <= segment[-1][1]:
                s.pop(i)
            else:
                i += 1
    return segment


def pointscover2(s):
    segment = []
    s.sort()
    i = 0
    while i < len(s):
        xm = s[i]
        segment.append([xm, xm+1])
        i += 1
        while i < len(s) and s[i] <= xm+1:
            i += 1
    return segment


s = [rnd.randint(0, 30) for i in range(10)]
s2 = s.copy()
print("Множество точек:", s)
seg = pointscover1(s)
print("Множество отрезков:", seg)
s = s2
seg = pointscover2(s)
print("Множество отрезков 2:", seg)
