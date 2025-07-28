class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        n = len(nums)
        for i in nums:
            ans |= i
        for i in range(1, 1 << n):
            cur = 0
            for j in range(n):
                if i & (1 << j):
                    cur |= nums[j]
            if cur == ans:
                count += 1
        return count
