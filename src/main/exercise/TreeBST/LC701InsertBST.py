from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    d = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([4,2,7,1,3])
    root2 = tree.generateBinaryTree([40,20,60,10,30,50,70])
    root3 = tree.generateBinaryTree([4,2,7,1,3])
    d.show(root1)
    print()
    d.show(root2)
    print()
    d.show(root3)
    print()
    d.show(s.insertIntoBST(root1, 5))
    d.show(s.insertIntoBST(root2, 25))
    d.show(s.insertIntoBST(root3, 5))

