import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            if total_hours > h:
                left = mid+1
            else:
                right = mid-1
        return left
