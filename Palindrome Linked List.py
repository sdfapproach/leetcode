# https://leetcode.com/problems/palindrome-linked-list/?envType=daily-question&envId=2024-03-22
# Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # li = []

        # while head:
        #     li.append(head.val)
        #     head = head.next

        # return li == list(reversed(li))

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True