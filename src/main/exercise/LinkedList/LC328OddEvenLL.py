from model.ListNode import ListNode
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd_head = head
        even_head = head.next
        temp_odd = odd_head
        temp_even = even_head

        while temp_even is not None and temp_even.next is not None:
            temp_odd.next = temp_even.next
            temp_odd = temp_even.next

            temp_even.next = temp_odd.next
            temp_even = temp_odd.next
        temp_odd.next = even_head
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode().createSinglyList([1, 2, 3, 4, 5])
    l2 = ListNode().createSinglyList([1, 2])
    l3 = ListNode().createSinglyList([1, 2, 3])
    l4 = ListNode().createSinglyList([1, 2, 3, 4])
    # print(ListNode().displaySinglyList(l1))

    print(ListNode().displaySinglyList(s.oddEvenList(l1)))
    print(ListNode().displaySinglyList(s.oddEvenList(l2)))
    print(ListNode().displaySinglyList(s.oddEvenList(l3)))
    print(ListNode().displaySinglyList(s.oddEvenList(l4)))
