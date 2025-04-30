# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/?envType=daily-question&envId=2025-04-30
# Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count
