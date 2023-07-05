from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        lst = self.path_sum(root)
        for num in lst:
            if num == targetSum:
                return True
        return False

    def path_sum(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [root.val]

        left = self.path_sum(root.left)
        for l in left:
            res.append(root.val + l)

        right = self.path_sum(root.right)
        for r in right:
            res.append(root.val + r)
        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    diagram.show(root1)
    print()
    print(s.hasPathSum(root1, 22))
