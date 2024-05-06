# https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06
# Remove Nodes From Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        
        max_val = float('-inf')
        new_head = None
        
        while stack:
            node = stack.pop()
            if node.val >= max_val:
                node.next = new_head
                new_head = node
                max_val = node.val
        
        return new_head