class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        csum = 0
        max_sum = 0
        s = set()
        for right in range(len(nums)):
            while nums[right] in s:
                csum -= nums[left]
                s.remove(nums[left])
                left += 1
            csum += nums[right]
            s.add(nums[right])
            max_sum = max(csum, max_sum)

        return max_sum
