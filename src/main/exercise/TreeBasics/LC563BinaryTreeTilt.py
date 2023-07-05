from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        self.replace(root)
        return self.sum_all(root)

    def replace(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        if not root.left and not root.right:
            root.val = 0
            return
        root.val = abs(self.sum_all(root.left) - self.sum_all(root.right))
        self.replace(root.left)
        self.replace(root.right)

    def sum_all(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        return root.val + self.sum_all(root.left) + self.sum_all(root.right)


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([1,2,3])
    root2 = tree.generateBinaryTree([4,2,9,3,5,None,7])
    root3 = tree.generateBinaryTree([21,7,14,1,1,2,2,3,3])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    print(s.findTilt(root1))
    print(s.findTilt(root2))
    print(s.findTilt(root3))
