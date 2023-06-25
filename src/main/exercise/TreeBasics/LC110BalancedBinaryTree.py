from model.TreeNode import TreeNode
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.BinaryTreeDiagram import BinaryTreeDiagram
from typing import Optional, List


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                l_height = self.height_helper(root.left)
                r_height = self.height_helper(root.right)
            else:
                return False
            return abs(l_height - r_height) <= 1

    def height_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            l_height = self.height_helper(root.left)
            r_height = self.height_helper(root.right)
            return 1 + max(l_height, r_height)


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([3,9,20,None,None,15,7])
    root2 = tree.generateBinaryTree([1,2,2,3,3,None,None,4,4])
    root3 = tree.generateBinaryTree([])
    root4 = tree.generateBinaryTree([1,2,2,3,None,None,3,4,None,None,4])
    root5 = tree.generateBinaryTree([1,None,2,None,3])
    # s = Solution()
    # print(s.isBalanced(root1))  # true
    # print(s.isBalanced(root2))  # false
    # print(s.isBalanced(root3))  # true
    # print(s.isBalanced(root4))  # false
    # print(s.isBalanced(root5))  # false

    diagram = BinaryTreeDiagram()
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    diagram.show(root4)
    print()
    diagram.show(root5)


