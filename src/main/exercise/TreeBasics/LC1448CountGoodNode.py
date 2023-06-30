from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.count_good = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.count_good

    def dfs(self, root: TreeNode, max_so_far: int) -> None:
        if root.val >= max_so_far:
            self.count_good += 1
        if root.left is not None:
            max_so_far = max(max_so_far, root.val)
            self.dfs(root.left, max_so_far)
        if root.right is not None:
            max_so_far = max(max_so_far, root.val)
            self.dfs(root.right, max_so_far)


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()

    # root1 = tree.generateBinaryTree([3,1,4,3,None,1,5])
    # root2 = tree.generateBinaryTree([3,3,None,4,2])
    # root3 = tree.generateBinaryTree([1])
    # root4 = tree.generateBinaryTree([9,None,3,6])
    root5 = tree.generateBinaryTree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
    # diagram.show(root1)
    # print()
    # diagram.show(root2)
    # print()
    # diagram.show(root3)
    # print()
    diagram.show(root5)
    print()
    # res1 = s.goodNodes(root1)
    # print(res1)
    # res2 = s.goodNodes(root2)
    # print(res2)
    # res3 = s.goodNodes(root3)
    # print(res3)
    # res4 = s.goodNodes(root4)
    # print(res4)
    res5 = s.goodNodes(root5)
    print(res5)
