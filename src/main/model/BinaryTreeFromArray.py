from typing import List, Optional
from model.TreeNode import TreeNode


class BinaryTreeFromArray:
    """
    https://leetcode.cn/circle/discuss/vpcMyM/
    Author: Long Luo (羽路阳光)
    """
    def generateBinaryTree(self, arr: List[int]) -> Optional[TreeNode]:
        arr_length = len(arr)
        if not arr or arr_length == 0 or arr[0] is None:
            return None

        index = 0
        root = TreeNode(arr[0])
        node_queue = [root]
        while index < arr_length:
            curr = node_queue.pop(0)
            # handle left child
            index += 1
            if index >= arr_length:
                return root
            left_child = arr[index]
            if left_child is not None:
                curr.left = TreeNode(left_child)
                node_queue.append(curr.left)

            # handle right child
            index += 1
            if index >= arr_length:
                return root
            right_child = arr[index]
            if right_child is not None:
                curr.right = TreeNode(right_child)
                node_queue.append(curr.right)
        return root

    # def generateBinaryTree(self, arr: List[int]) -> TreeNode:
    #     # if not arr:
    #     #     return None
    #     root = TreeNode(arr[0])
    #     self.generate(root, 1, arr)
    #     return root

    # def generate(self, root: TreeNode, rootIndex: int, arr: List[int]) -> None:
    #     n = len(arr)
    #     leftIndex = 2 * rootIndex + 1
    #     if leftIndex < n and arr[leftIndex] is not None:
    #         root.left = TreeNode(arr[leftIndex])
    #         self.generate(root.left, leftIndex, arr)
    #
    #     rightIndex = 2 * rootIndex + 2
    #     if rightIndex < n and arr[rightIndex] is not None:
    #         root.right = TreeNode(arr[rightIndex])
    #         self.generate(root.right, rightIndex, arr)

