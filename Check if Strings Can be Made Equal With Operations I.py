# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/?envType=daily-question&envId=2026-03-29
# Check if Strings Can be Made Equal With Operations I

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
        
        return True