# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            left_height, left_balanced = dfs(root.left)
            right_height, right_balanced = dfs(root.right)
            current_height = 1+max(left_height, right_height)
            if abs(left_height-right_height) > 1:
                return current_height, False
            return current_height, left_balanced and right_balanced
        h, bal = dfs(root)
        return bal
