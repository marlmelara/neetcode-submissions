# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        # Reverse list first
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reverse list again and skip over the nth node to remove from list

        curr = prev # Current head of reversed list
        prev = None # Reset prev
        count = 1 # Starting node value

        while curr:
            next_node = curr.next

            if count != n:
                curr.next = prev
                prev = curr

            curr = next_node 
            count += 1

        return prev