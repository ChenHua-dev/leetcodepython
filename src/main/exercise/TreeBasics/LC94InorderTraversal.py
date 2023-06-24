from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if not root:
            return []
        else:
            lst.extend(self.inorderTraversal(root.left))
            lst.append(root.val)
            lst.extend(self.inorderTraversal(root.right))
            return lst
