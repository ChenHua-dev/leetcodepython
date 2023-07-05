from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left = self.binaryTreePaths(root.left)
        for l in left:
            res.append(str(root.val) + "->" + l)

        right = self.binaryTreePaths(root.right)
        for l in right:
            res.append(str(root.val) + "->" + l)

        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()

    root1 = tree.generateBinaryTree([1,2,3,None,5])
    root2 = tree.generateBinaryTree([1,None,3])
    root3 = tree.generateBinaryTree([])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    print(s.binaryTreePaths(root1))
    print(s.binaryTreePaths(root2))
    print(s.binaryTreePaths(root3))
