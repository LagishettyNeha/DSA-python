n = [2, 4, 6, 8, 10]
n = set(n)
mini = min(n)
maxi = max(n)
i = 2
while True:
    if i not in n:
        print(i)
    i += 2
