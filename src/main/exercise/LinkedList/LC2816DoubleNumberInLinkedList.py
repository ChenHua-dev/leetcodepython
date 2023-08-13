from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        fake_head = self.reverse(head)
        temp = fake_head
        carry = 0
        while temp is not None:
            digit = temp.val * 2
            digit += carry
            carry = digit // 10
            temp.val = digit % 10
            temp = temp.next

        fake_head2 = fake_head
        if carry != 0:
            while fake_head2.next is not None:
                fake_head2 = fake_head2.next
            fake_head2.next = ListNode(carry)
            fake_head2 = fake_head2.next

        return self.reverse(fake_head)

    def reverse(self, head):
        fake = None
        prev = head
        curr = head
        while prev is not None:
            curr = curr.next
            prev.next = fake
            fake = prev
            prev = curr
        return fake
