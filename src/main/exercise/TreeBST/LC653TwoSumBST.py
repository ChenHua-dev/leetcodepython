from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional


class Solution:
    def __init__(self):
        self.m = {}

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        complement = k - root.val
        if complement not in self.m:
            self.m[root.val] = True
            return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([5,3,6,2,4,None,7])
    root2 = tree.generateBinaryTree([5,3,6,2,4,None,7])
    root3 = tree.generateBinaryTree([2,1,3])
    root4 = tree.generateBinaryTree([1])
    root5 = tree.generateBinaryTree([2,0,3,-4,1])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    diagram.show(root4)
    print()
    diagram.show(root5)
    print()
    print(s.findTarget(root1, 9))  # expect: true
    print(s.findTarget(root2, 28))  # expect: false
    print(s.findTarget(root3, 4))  # expect: true
    print(s.findTarget(root4, 2))  # expect: false
    print(s.findTarget(root5, -1))  # expect: true
