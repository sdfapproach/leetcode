# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12
# Remove Zero Sum Consecutive Nodes from Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # nums = []

        # while head != None:
        #     nums.append(head.val)
        #     head = head.next

        # nums.sort()
        
        # minus = nums[0]

        # node = ListNode()

        # return node

        seen = {}
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        total = 0
        
        while curr:
            total += curr.val
            if total in seen:
                prev = seen[total].next
                temp = total + prev.val
                while temp != total:
                    del seen[temp]
                    prev = prev.next
                    temp += prev.val
                seen[total].next = curr.next
            else:
                seen[total] = curr
            curr = curr.next
        
        return dummy.next