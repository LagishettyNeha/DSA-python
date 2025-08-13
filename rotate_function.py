class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        tsum = sum(nums)
        n = len(nums)
        f = sum(i*num for i, num in enumerate(nums))
        res = f
        for k in range(1, n):
            f = f+tsum-n*nums[-k]
            res = max(res, f)
        return res
