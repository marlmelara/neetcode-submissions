# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the list
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reverse it back and remove nth node

        curr = prev # Current head of reversed list
        count = 1 # Count of nth node we are on
        prev = None # Reset prev

        while curr:
            next_node = curr.next

            if count != n:
                curr.next = prev
                prev = curr

            curr = next_node
            count += 1

        return prev