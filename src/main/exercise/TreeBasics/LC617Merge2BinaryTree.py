from model.TreeNode import TreeNode
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1 and root2 is not None:
            return root2
        if not root2 and root1 is not None:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([1,3,2,5])
    root2 = tree.generateBinaryTree([2,1,3,None,4,None,7])
    # root3 = tree.generateBinaryTree([1])
    # root4 = tree.generateBinaryTree([1,2])
    d = BinaryTreeDiagram()
    # d.show(root1)
    # print()
    # d.show(root2)
    # print()
    # d.show(root3)
    # print()
    # d.show(root4)
    print()
    s = Solution()
    print(d.show(s.mergeTrees(root1, root2)))
    # print(d.show(s.mergeTrees(root3, root4)))
