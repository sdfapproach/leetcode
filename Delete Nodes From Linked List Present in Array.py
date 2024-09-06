# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06
# Delete Nodes From Linked List Present in Array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy = ListNode()
        # tail = dummy

        # while head:
        #     if head.val not in nums:
        #         tail.next = ListNode(head.val)
        #         tail = tail.next
        #     head = head.next

        # return dummy.next

        nums_set = set(nums)
        dummy = ListNode()
        tail = dummy

        while head:
            if head.val not in nums_set:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None
        return dummy.next