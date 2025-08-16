
class Solution:
    def maximum69Number(self, num: int) -> int:
        n = list(str(num))
        maxi = num
        for i in range(len(n)):
            temp = n[:]
            if temp[i] == 9:
                temp[i] = 6
            else:
                temp[i] = 9
            maxi = max(maxi, int(''.join(map(str, temp))))
        return maxi
