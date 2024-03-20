# https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20
# Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        node = ListNode(0)
        node.next = list1
        prev = node

        for i in range(a):
            prev = prev.next

        end = prev.next

        for _ in range(b-a+1):
            end = end.next

        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        prev.next = list2
        list2_tail.next = end

        return node.next