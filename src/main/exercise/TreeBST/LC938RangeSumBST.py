from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional


class Solution:
    def __init__(self) -> None:
        self.total = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.helper(root, low, high)
        return self.total

    def helper(self, root: Optional[TreeNode], low: int, high: int) -> None:
        if not root:
            return
        if root.val >= low and root.val <= high:
            self.total += root.val
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([10,5,15,3,7,None,18])
    root2 = tree.generateBinaryTree([10,5,15,3,7,13,18,1,None,6])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    print(s.rangeSumBST(root1, 7, 15))  # expected 32
    print(s.rangeSumBST(root2, 6, 10))  # expected 23
