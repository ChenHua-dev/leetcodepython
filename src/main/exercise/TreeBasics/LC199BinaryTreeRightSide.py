from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            cur_level = []
            len_level = len(queue)

            for _ in range(len_level):
                temp_node = queue.pop(0)
                cur_level.append(temp_node.val)

                if temp_node.left is not None:
                    queue.append(temp_node.left)
                if temp_node.right is not None:
                    queue.append(temp_node.right)
            res.append(cur_level[-1])
        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()

    root1 = tree.generateBinaryTree([1,2,3,None,5,None,4])
    root2 = tree.generateBinaryTree([1,None,3])
    root3 = tree.generateBinaryTree([])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    print(s.rightSideView(root1))
    print(s.rightSideView(root2))
    print(s.rightSideView(root3))






