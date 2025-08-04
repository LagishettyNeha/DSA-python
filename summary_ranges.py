class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        for n in nums:
            if r and r[-1][1] == n-1:
                r[-1][1] = n
            else:
                r.append([n, n])
        return [f'{x}->{y}' if x != y else f'{x}' for x, y in r]
