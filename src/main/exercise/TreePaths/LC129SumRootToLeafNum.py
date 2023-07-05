from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = self.helper(root)
        total = 0
        for s in lst:
            total += int(s)
        return total

    def helper(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left = self.helper(root.left)
        for l in left:
            res.append(str(root.val) + l)

        right = self.helper(root.right)
        for r in right:
            res.append(str(root.val) + r)

        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([1,2,3])
    root2 = tree.generateBinaryTree([4,9,0,5,1])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    print(s.sumNumbers(root1))  # expect: 25
    print(s.sumNumbers(root2))  # expect: 1026
