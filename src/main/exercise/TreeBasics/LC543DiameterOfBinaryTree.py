from model.TreeNode import TreeNode
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from typing import Optional


class Solution:
    global_max = 0

    def get_longest_path(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_path = self.get_longest_path(root.left)
        right_path = self.get_longest_path(root.right)
        local_max = left_path + right_path
        self.global_max = max(self.global_max, local_max)
        return 1 + max(left_path, right_path)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_longest_path(root)
        return self.global_max


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    # lst = [1,2,3,4,5,6,7,8,None,9,None,None,12,None,None,10,None,11]
    # lst = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    lst = [1,2,3,4,5]
    root1 = tree.generateBinaryTree(lst)
    diagram = BinaryTreeDiagram()
    diagram.show(root1)
    print()
    s = Solution()
    print(s.diameterOfBinaryTree(root1))

