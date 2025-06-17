class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        hm = set()
        for i in jewels:
            hm.add(i)
        for i in stones:
            if i in hm:
                count += 1
        return count
