from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def all_paths(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        left = self.all_paths(root.left)
        for l in left:
            l.insert(0, root.val)
            res.append(l)

        right = self.all_paths(root.right)
        for r in right:
            r.insert(0, root.val)
            res.append(r)

        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    d = BinaryTreeDiagram()

    root1 = tree.generateBinaryTree([3,1,4,3,None,1,5])
    root2 = tree.generateBinaryTree([3,3,None,4,2])
    root3 = tree.generateBinaryTree([9,None,3,6])
    root4 = tree.generateBinaryTree([1])
    d.show(root1)
    print()
    d.show(root2)
    print()
    d.show(root3)
    print()
    d.show(root4)
    print()
    print(s.all_paths(root1))
    print(s.all_paths(root2))
    print(s.all_paths(root3))
    print(s.all_paths(root4))
