# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/?envType=daily-question&envId=2026-08-31
# Find the Minimum and Maximum Number of Nodes Between Critical Points

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1
        min_distance = float('inf')

        while curr.next:
            nxt = curr.next

            is_max = curr.val > prev.val and curr.val > nxt.val
            is_min = curr.val < prev.val and curr.val < nxt.val

            if is_max or is_min:
                if first == -1:
                    first = index
                else:
                    min_distance = min(
                        min_distance,
                        index - last
                    )

                last = index

            prev = curr
            curr = nxt
            index += 1

        if first == last:
            return [-1, -1]

        return [
            min_distance,
            last - first
        ]