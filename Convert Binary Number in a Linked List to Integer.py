# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/?envType=daily-question&envId=2025-07-14
# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        bit = ""

        node = head

        while node:
            bit += str(node.val)
            node = node.next
       
        return int(bit, 2)