class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        total = 1
        zc = 0
        for n in nums:
            if n != 0:
                total *= n
            else:
                zc += 1
        if zc > 1:
            return [0]*len(nums)
        for n in nums:
            if n != 0:
                if zc == 1:
                    ans.append(0)
                else:
                    ans.append(total//n)
            else:
                ans.append(total)
        return ans
