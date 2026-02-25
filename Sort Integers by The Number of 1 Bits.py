# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2026-02-25
# Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))