# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=daily-question&envId=2024-03-03
# Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # def get_node(node, li = []):

        #     if node:
        #         li.append(node.val)
        #         get_node(node.next, li)

        #     return li

        # def list_to_linked_list(li):
        #     if len(li) <= 0:
        #         return ListNode()

        #     head = ListNode(li[0])
        #     current = head
        #     for num in li[1:]:
        #         current.next = ListNode(li)
        #         current = current.next
        #     return head

        # listed = get_node(head)
        # listed.pop(len(listed)-n)

        # return list_to_linked_list(listed)

        def list_to_linked_list(li):
            if len(li) <= 0:
                return None

            head = ListNode(li[0])
            current = head
            for num in li[1:]:
                current.next = ListNode(num)
                current = current.next
            return head

        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        for _ in range(length - n):
            current = current.next

        current.next = current.next.next

        return dummy.next