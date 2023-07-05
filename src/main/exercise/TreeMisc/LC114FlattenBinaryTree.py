from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)

        root.left = None
        root.right = left
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([1,2,5,3,4,None,6])
    root2 = tree.generateBinaryTree([2,1])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    s.flatten(root1)
    s.flatten(root2)
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
