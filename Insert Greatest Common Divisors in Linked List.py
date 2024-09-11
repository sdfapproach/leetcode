# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/?envType=daily-question&envId=2024-09-10
# Insert Greatest Common Divisors in Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(head.val)
        node = dummy
        
        # def gcd(a, b) -> int:

        #     i = min(a, b)

        #     while a % i != 0 or b % i != 0:
        #         i -= 1
            
        #     return i

        # while head.next:

        #     print(node)
            
        #     gcd_node = ListNode(gcd(head.val, head.next.val))
        #     gcd_node.next = head.next

        #     head = head.next

        # return node

        while head and head.next:
            next_node = head.next
            
            node.next = ListNode(head.val)
            node = node.next
            
            gcd_value = math.gcd(head.val, head.next.val)
            gcd_node = ListNode(gcd_value)
            node.next = gcd_node
            node = node.next

            head = next_node

        node.next = ListNode(head.val)

        return dummy.next