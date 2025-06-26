import sys
n = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append(a)


def coupon(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if hasAll(str(arr[i])+str(arr[j])):
                count += 1
    return count


def hasAll(s):
    return set('0123456789').issubset(set(s))


ans = coupon(arr)
print(ans)
