# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/?envType=daily-question&envId=2026-04-15
# Shortest Distance to Target String in a Circular Array

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        
        for step in range(n):
            if words[(startIndex + step) % n] == target:
                return step
            if words[(startIndex - step + n) % n] == target:
                return step
        
        return -1