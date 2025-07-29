class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        k = 0
        i = 0
        seen = deque([])
        ans = []
        for num in nums:
            if num != -1:
                seen.appendleft(num)
                i = 0
            else:
                i += 1
                if i > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[i-1])

        return ans
