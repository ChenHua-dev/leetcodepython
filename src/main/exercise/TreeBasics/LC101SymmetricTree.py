from model.TreeNode import TreeNode
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        check_root = (root1.val == root2.val)
        check_outer = self.is_mirror(root1.left, root2.right)
        check_inner = self.is_mirror(root1.right, root2.left)
        return check_root and check_outer and check_inner


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([1,2,2,3,4,4,3])
    root2 = tree.generateBinaryTree([1,2,2,None,3,None,3])
    d = BinaryTreeDiagram()
    d.show(root1)
    print()
    d.show(root2)

    s = Solution()
    print(s.isSymmetric(root1))
    print(s.isSymmetric(root2))
