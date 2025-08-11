class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        MOD = 10**9+7
        arr = [1 << i for i in range(31) if (1 << i) & n]
        print(arr)
        for l, r in queries:
            product = 1
            for i in range(l, r+1):
                product = (arr[i]*product) % MOD
            ans.append(product)
        return ans
