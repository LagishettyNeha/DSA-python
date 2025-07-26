class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        li = []
        nums.sort()
        for i in range(len(nums)-3):

            l = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        li.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1

                    elif total < target:
                        k += 1
                    elif total > target:
                        l -= 1

        return li
