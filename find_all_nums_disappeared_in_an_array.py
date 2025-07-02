class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(range(1, len(nums)+1))
        res = list(ans-set(nums))
        return res
