# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2025-03-26
# Minimum Operations to Make a Uni-Value Grid

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = [num for row in grid for num in row]
        
        mod = arr[0] % x
        for num in arr:
            if num % x != mod:
                return -1
        
        arr.sort()
        median = arr[len(arr) // 2]
        
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops