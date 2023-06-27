from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if not root:
            return []
        else:
            lst.append(root.val)
            lst.append(self.preorderTraversal(root.left))
            lst.append(self.preorderTraversal(root.right))
            return lst


if __name__ == '__main__':
    # root = TreeNode(1)
    # rootL = TreeNode(None)
    # rootR = TreeNode(2)
    # root.left = rootL
    # root.right = rootR
    # rootR.left = TreeNode(3)
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([3,9,20,None,None,15,7])
    root2 = tree.generateBinaryTree([8,5,10,1,7,None,12])
    root3 = tree.generateBinaryTree([1,2,8,3,4,9,None,5,None,None,None,None,None,6,7])

    diagram = BinaryTreeDiagram()
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
