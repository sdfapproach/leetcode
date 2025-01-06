# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-06
# Minimum Number of Operations to Move All Balls to Each Box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        answer = [0] * n

        count = 0
        operations = 0

        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count
        
        count = 0
        operations = 0

        for i in range(n-1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count
        
        return answer