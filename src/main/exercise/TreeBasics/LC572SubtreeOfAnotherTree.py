from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def is_same(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        is_left_same = self.is_same(root.left, subRoot.left)
        is_right_same = self.is_same(root.right, subRoot.right)
        return is_left_same and is_right_same

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.is_same(root, subRoot):
            return True

        check_left_child = self.isSubtree(root.left, subRoot)
        check_right_child = self.isSubtree(root.right, subRoot)
        return check_left_child or check_right_child


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([3,4,5,1,2])
    sub1 = tree.generateBinaryTree([4,1,2])
    print(s.isSubtree(root1, sub1))

    root2 = tree.generateBinaryTree([3,4,5,1,2,None,None,None,None,0])
    sub2 = tree.generateBinaryTree([4,1,2])
    # sub3 = tree.generateBinaryTree([4,1,2,None,None,0])
    print(s.isSubtree(root2, sub2))

    diagram = BinaryTreeDiagram()
    diagram.show(root1)
    print()
    diagram.show(sub1)
    print()
    diagram.show(root2)
    print()
    diagram.show(sub2)
