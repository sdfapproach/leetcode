# https://leetcode.com/problems/middle-of-the-linked-list/?envType=daily-question&envId=2024-03-07
# Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # length = 0

        # node = head

        # while node:
        #     node = node.next
        #     length += 1

        # for i in range(length//2):
        #     head = head.next

        # return head

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow