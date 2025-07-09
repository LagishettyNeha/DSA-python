import math
arr = [5, 6, 7, 8, 9]
x = 2
single = 0
dynamic = 0
for i in range(len(arr)):
    single += math.ceil(arr[i]/x)
print(single)
print(max(arr))
