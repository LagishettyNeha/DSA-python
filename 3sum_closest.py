class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindif = float('inf')
        csum = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                cdif = abs(total-target)
                if cdif < mindif:
                    mindif = cdif
                    csum = total
                if total < target:
                    j += 1
                else:
                    k -= 1
        return csum
