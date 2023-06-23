from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        lst.append(root.val)
        if root == None:
            return lst
        else:
            if not root.left:
                lst.append(self.preorderTraversal(root.left))
            if not root.right:
                lst.append(self.preorderTraversal(root.right))
