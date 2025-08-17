class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k-1+maxPts:
            return 1.0
        dp = [0.0]*maxPts
        dp[0] = 1.0
        wsum = 1.0
        res = 0.0
        for i in range(1, n+1):
            prob = wsum/maxPts
            if i < k:
                wsum += prob
            else:
                res += prob
            if i >= maxPts:
                wsum -= dp[i % maxPts]
            dp[i % maxPts] = prob
        return res
