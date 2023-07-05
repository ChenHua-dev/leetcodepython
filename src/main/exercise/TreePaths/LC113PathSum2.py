from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        lst = self.dfs_helper(root)
        for l in lst:
            if sum(l) == targetSum:
                res.append(l)
        return res

    def dfs_helper(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [[root.val]]

        left = self.dfs_helper(root.left)
        for l in left:
            l.insert(0, root.val)
            res.append(l)

        right = self.dfs_helper(root.right)
        for r in right:
            r.insert(0, root.val)
            res.append(r)
        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    diagram.show(root1)
    print()
    print(s.pathSum(root1, 22))
