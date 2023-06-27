from model.TreeNode import TreeNode
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        is_same_left = self.isSameTree(p.left, q.left)
        is_same_right = self.isSameTree(p.right, q.right)
        return is_same_left and is_same_right
