from __future__ import annotations
from typing import Any, List, Optional


class ListNode:
    val: Any
    next: Optional[ListNode]

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def createSinglyList(self, lst: List[int]) -> ListNode:
        if not lst:
            head = None
        else:
            head = ListNode(lst[0])
            cur = head
            for i in range(1, len(lst)):
                cur.next = ListNode(lst[i])
                cur = cur.next
        return head

    def displaySinglyList(self, head: Optional[ListNode]) -> str:
        items = []
        cur = head
        while cur is not None:
            items.append(str(cur.val))
            cur = cur.next
        return '[' + ' -> '.join(items) + ']'


