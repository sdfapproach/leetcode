# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/?envType=daily-question&envId=2024-05-07
# Double a Number Represented as a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # num = ""

        # while head:
        #     num += str(head.val)
        #     head = head.next

        # num = str(int(num) * 2)

        # new_node = ListNode(int(num[0]))
        # current = new_node

        # for i in range(1, len(num)):
        #     node = ListNode(int(num[i]))
        #     current.next = node
        #     current = node

        # return new_node

        def reverseList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        head = reverseList(head)

        current = head
        carry = 0
        while current:
            new_val = current.val * 2 + carry
            current.val = new_val % 10
            carry = new_val // 10
            last = current
            current = current.next
        
        if carry > 0:
            last.next = ListNode(carry)

        return reverseList(head)