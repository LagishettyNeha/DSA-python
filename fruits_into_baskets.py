class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in baskets:
                if fruits[i] <= j:
                    baskets.remove(j)
                    break
        return len(baskets)
