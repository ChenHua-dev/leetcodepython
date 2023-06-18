from model.ListNode import ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revHead = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = revHead
            revHead = curr
            curr = temp
        return revHead


if __name__ == '__main__':
    head = ListNode().createSinglyList([1, 2, 3, 4, 5])
    print(ListNode().displaySinglyList(head))
    print(ListNode().displaySinglyList(Solution().reverseList(head)))
