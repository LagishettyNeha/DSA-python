'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    # Function to return the level order traversal line by line of a tree.
    def levelOrder(self, root):

        # code here
        res = []
        queue = deque([root])
        while queue:
            lev_size = len(queue)
            row = []
            for i in range(lev_size):
                cur = queue.popleft()
                row.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(row)
        return res
