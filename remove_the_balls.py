
class Solution:
    def findLength(self, color, radius):
        stack = []
        for i in range(len(color)):
            if stack and color[i] == color[stack[-1]] and radius[i] == radius[stack[-1]]:
                stack.pop()
            else:
                stack.append(i)

        return len(stack)
