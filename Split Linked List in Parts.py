# https://leetcode.com/problems/split-linked-list-in-parts/?envType=daily-question&envId=2024-09-08
# Split Linked List in Parts

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        
        part_length = length // k
        extra_nodes = length % k
        
        parts = []
        current = head

        for i in range(k):
            part_head = current
            part_size = part_length + (1 if i < extra_nodes else 0)
            
            for j in range(part_size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            parts.append(part_head)
        
        return parts