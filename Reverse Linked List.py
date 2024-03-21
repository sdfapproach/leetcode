# https://leetcode.com/problems/reverse-linked-list/?envType=daily-question&envId=2024-03-21
# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # nums = []

        # while head:
        #     nums.append(head.val)
        #     head = head.next

        # if len(nums) < 1:
        #     return 

        # nums.reverse()

        # node = ListNode(nums[0])
        # current = node

        # for n in nums[1:]:
        #     current.next = ListNode(n)
        #     current = current.next

        # return node


        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev