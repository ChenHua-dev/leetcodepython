from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self, root, ) -> int:
        if not root:
            return 0

        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        self.ans = max(left_max + right_max + root.val, self.ans)
        return max(left_max, right_max) + root.val
