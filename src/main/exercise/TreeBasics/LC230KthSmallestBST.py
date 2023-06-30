from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = self.inorder(root)
        return lst[k - 1]

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        res.extend(self.inorder(root.left))
        res.append(root.val)
        res.extend(self.inorder(root.right))
        return res
