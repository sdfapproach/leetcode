# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/?envType=daily-question&envId=2025-12-07
# Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        odds = 0

        if low % 2 ==1:
            odds += 1
        elif high % 2 ==1:
            odds += 1

        odds += (high - low) // 2

        return odds