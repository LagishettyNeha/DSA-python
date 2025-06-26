class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        res = []
        for k, v in sorted(count.items(), key=lambda x: x[-1], reverse=True):
            res += [k]*v
        return "".join(res)
