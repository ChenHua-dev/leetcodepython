from typing import List
from model.TreeNode import TreeNode


class BinaryTreeFromArray:
    def generateBinaryTree(self, arr: List[int]) -> TreeNode:
        root = TreeNode(arr[0])
        self.generate(root, 0, arr)
        return root

    def generate(self, root: TreeNode, rootIndex: int, arr: List[int]) -> None:
        n = len(arr)
        leftIndex = 2 * rootIndex + 1
        if leftIndex < n and arr[leftIndex] is not None:
            root.left = TreeNode(arr[leftIndex])
            self.generate(root.left, leftIndex, arr)

        rightIndex = 2 * rootIndex + 2
        if rightIndex < n and arr[rightIndex] is not None:
            root.right = TreeNode(arr[rightIndex])
            self.generate(root.right, rightIndex, arr)

