def towersOfHanoi(n, t1, t2, t3):
    if n == 1:
        t3.append(t1.pop())
    else:
        towersOfHanoi(n - 1, t1, t3, t2)
        t3.append(t1.pop())
        towersOfHanoi(n - 1, t2, t1, t3)


t1 = [0, 1, 2, 3, 4, 5]
t2 = []
t3 = []
towersOfHanoi(len(t1), t1, t2, t3)
print(t1, t2, t3)
