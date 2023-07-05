import math

from model.TreeNode import TreeNode
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from typing import Optional

class Solution:
    def is_valid_helper(self, root: Optional[TreeNode], left = -math.inf, right = math.inf) -> bool:
        if not root:
            return True
        # Base case:
        # valid BST is when left < root < right
        # invalid is when left >= root or root >= right
        if left >= root.val or root.val >= right:
            return False

        # Recursive case:
        is_left_valid = self.is_valid_helper(root.left, left, root.val)
        is_right_valid = self.is_valid_helper(root.right, root.val, right)
        return is_left_valid and is_right_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_helper(root)


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([2, 1, 3])
    root2 = tree.generateBinaryTree([5, 1, 4, None, None, 3, 6])
    d = BinaryTreeDiagram()
    d.show(root1)
    print()
    d.show(root2)

    s = Solution()
    print(s.isValidBST(root1))
    print(s.isValidBST(root2))

