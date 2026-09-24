# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        prev1, prev2 = None, None
        # Reverse both lists
        while curr1:
            next_node = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = next_node

        while curr2:
            next_node = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = next_node

        num1_str, num2_str = "", ""
        curr1, curr2 = prev1, prev2

        while curr1:
            num1_str += str(curr1.val)
            curr1 = curr1.next

        while curr2:
            num2_str += str(curr2.val)
            curr2 = curr2.next

        num1, num2 = int(num1_str), int(num2_str)
        result = num1 + num2
        result_to_str = str(result)

        dummy = ListNode()
        tail = dummy

        for i in range(len(result_to_str) - 1, -1, -1):
            tail.next = ListNode(int(result_to_str[i]))
            tail = tail.next

        return dummy.next
