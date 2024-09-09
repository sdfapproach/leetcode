# https://leetcode.com/problems/spiral-matrix-iv/?envType=daily-question&envId=2024-09-09
# Spiral Matrix IV

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        top, bottom, left, right = 0, m - 1, 0, n - 1
    
        i, j = 0, 0

        direction = 0
        
        while head:
            matrix[i][j] = head.val
            head = head.next

            if direction == 0:
                if j < right:
                    j += 1
                else:
                    direction = 1
                    top += 1
                    i += 1
            elif direction == 1:
                if i < bottom:
                    i += 1
                else:
                    direction = 2
                    right -= 1
                    j -= 1
            elif direction == 2:
                if j > left:
                    j -= 1
                else:
                    direction = 3
                    bottom -= 1
                    i -= 1
            elif direction == 3:
                if i > top:
                    i -= 1
                else:
                    direction = 0
                    left += 1
                    j += 1

        return matrix