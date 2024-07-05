# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/?envType=daily-question&envId=2024-07-05
# Find the Minimum and Maximum Number of Nodes Between Critical Points

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        points = []

        i = 2
        prev_prev_val = head.val
        head = head.next

        prev_val = head.val
        head = head.next

        while head:

            if (head.val > prev_val and prev_val < prev_prev_val) or (head.val < prev_val and prev_val > prev_prev_val):
                points.append(i-2)

            prev_prev_val = prev_val
            prev_val = head.val
            head = head.next
            i += 1

        if len(points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        for j in range(1, len(points)):
            min_distance = min(min_distance, points[j] - points[j-1])

        max_distance = points[-1] - points[0]

        return [min_distance, max_distance]