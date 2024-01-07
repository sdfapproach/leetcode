# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sum = []

        def get_num(head):
            current = head
            while current is not None:
                sum.append(current.val)
            
                current = current.next


        get_num(list1)
        get_num(list2)

        sum.sort()

        def set_num(num_list):
            linked_list = None
            for num in num_list[::-1]:
                linked_list = ListNode(num, linked_list)

            return linked_list

        return set_num(sum)