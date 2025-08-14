class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_ans = ""

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                ans = num[i:i+3]
                max_ans = max(max_ans, ans)
        return max_ans
