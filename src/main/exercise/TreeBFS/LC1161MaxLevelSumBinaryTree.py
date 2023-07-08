from model.TreeNode import TreeNode
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        level = 1
        max_level = -float('inf')
        max_sum = -float('inf')
        while queue:
            len_level = len(queue)
            cur_sum = 0
            for _ in range(len_level):
                temp_node = queue.pop(0)
                cur_sum += temp_node.val

                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            # print([cur_level, max_level])
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
            level += 1
        return max_level
