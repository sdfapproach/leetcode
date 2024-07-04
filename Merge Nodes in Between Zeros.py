# https://leetcode.com/problems/merge-nodes-in-between-zeros/?envType=daily-question&envId=2024-07-04
# Merge Nodes in Between Zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # nums = []
        # sum = 0

        # head = head.next
        
        # while head:

        #     val = head.val
            
        #     if val == 0:
        #         nums.append(sum)
        #         sum = 0
        #     else:
        #         sum += val

        #     head = head.next

        # nums = nums[::-1]
        # node = ListNode(nums[0])

        # for num in nums[1:]:

        #     new_node = ListNode(num)
        #     new_node.next = node
        #     node = new_node

        # return node

        head = head.next
        dummy = ListNode(0)
        node = dummy
        current_sum = 0
        
        while head:

            val = head.val
            
            if val == 0:
                node.next = ListNode(current_sum)
                node = node.next
                current_sum = 0
            else:
                current_sum += val

            head = head.next

        return dummy.next