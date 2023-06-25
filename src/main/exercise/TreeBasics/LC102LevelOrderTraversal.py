from model.TreeNode import TreeNode
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = [root]
        while len(queue) != 0:
            cur_level = []
            lvl_len = len(queue)
            for _ in range(lvl_len):
                temp = queue.pop(0)
                cur_level.append(temp.val)

                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            res.append(cur_level)

        return res
