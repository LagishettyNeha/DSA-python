class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and (abs(ord(i)-ord(stack[-1])) == 1 or abs(ord(i)-ord(stack[-1])) == 25):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
