
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional


class Solution:
    def __init__(self) -> None:
        self.lst = []
        self.min_diff = float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        for i in range(len(self.lst) - 1):
            self.min_diff = min(self.min_diff, self.lst[i+1] - self.lst[i])
        return self.min_diff
        # self.inorder(root)
        # self.traverse(root, self.lst, self.min_diff)
        # return self.min_diff

    # def traverse(self, root: Optional[TreeNode], lst: List[TreeNode], min_diff: int) -> None:
    #     for node in lst:
    #         if node.val != root.val:
    #             # print([node.val, root.val])
    #             self.min_diff = min(self.min_diff, abs(node.val - root.val))
    #             if root.left:
    #                 self.traverse(root.left, lst, self.min_diff)
    #             if root.right:
    #                 self.traverse(root.right, lst, self.min_diff)

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.inorder(root.left)
        self.lst.append(root.val)
        self.inorder(root.right)


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([4,2,6,1,3])
    root2 = tree.generateBinaryTree([1,0,48,None,None,12,49])
    root3 = tree.generateBinaryTree([1,None,3,2])
    root4 = tree.generateBinaryTree([236,104,701,None,227,None,911])
    root5 = tree.generateBinaryTree([1,None,5,3])
    root6 = tree.generateBinaryTree([1318,0,2065,None,924,None,4569,None,None,3811,None,3398,None,3271,None,2933,None,2596])
    root7 = tree.generateBinaryTree([0,None,100000])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    print(s.getMinimumDifference(root1))  # expected 1
    print(s.getMinimumDifference(root2))  # expected 1
    print(s.getMinimumDifference(root3))  # expected 1
    print(s.getMinimumDifference(root4))  # expected 9
    print(s.getMinimumDifference(root5))  # expected 2
    print(s.getMinimumDifference(root6))  # expected 127
    print(s.getMinimumDifference(root7))  # expected 100000

