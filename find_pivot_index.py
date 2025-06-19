class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0]*n
        suf = [0]*n
        for i in range(1, n):
            pre[i] = pre[i-1]+nums[i-1]
        for j in range(n-2, -1, -1):
            suf[j] = suf[j+1]+nums[j+1]
        for i in range(n):
            if pre[i] == suf[i]:
                return i
        return -1
