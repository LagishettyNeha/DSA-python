class Solution:
    def subarraySum(self, arr):
        # code here
        n = len(arr)
        x = 0
        y = n-1
        sum = 0
        for i in range(n):
            sum += (x+1)*(y+1)*(arr[i])
            x += 1
            y -= 1
        return sum
