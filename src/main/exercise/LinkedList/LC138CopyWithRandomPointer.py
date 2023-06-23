from model.RandomNode import Node
from typing import Optional


class Solution:
    def copyRandomList(self, head:'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy_map = {}

        curr = head
        while curr:
            copied = Node(curr.val)
            copy_map[curr] = copied
            curr = curr.next

        curr = head
        while curr:
            copied = copy_map.get(curr)
            copied.next = copy_map.get(copied.next, None)
            copied.random = copy_map.get(copied.random, None)
            curr = curr.next

        return copy_map.get(head)
