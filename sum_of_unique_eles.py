class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        sum = 0
        for i in hm:
            if hm[i] == 1:
                sum += i
        return sum
