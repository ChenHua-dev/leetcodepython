from model.TreeNode import TreeNode
from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        flip = 0
        while queue:
            len_level = len(queue)
            cur_level = []
            for _ in range(len_level):
                cur_node = queue.pop(0)
                cur_level.append(cur_node.val)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            if flip == 1:
                new_cur = []
                while cur_level:
                    new_cur.append(cur_level.pop())
                res.append(new_cur)
                flip = 0
            else:
                res.append(cur_level)
                flip = 1
        return res


if __name__ == '__main__':
    tree = BinaryTreeFromArray()
    root1 = tree.generateBinaryTree([3,9,20,None,None,15,7])
    root2 = tree.generateBinaryTree([1,2,3,4,5])
    root3 = tree.generateBinaryTree([1,2,3,4,None,None,5])
    d = BinaryTreeDiagram()
    d.show(root1)
    print()
    d.show(root2)
    print()
    d.show(root3)

    s = Solution()
    print(s.zigzagLevelOrder(root1))
    print(s.zigzagLevelOrder(root2))
    print(s.zigzagLevelOrder(root3))
