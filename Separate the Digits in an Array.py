# https://leetcode.com/problems/separate-the-digits-in-an-array/?envType=daily-question&envId=2026-05-11
# Separate the Digits in an Array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        digits = []

        for num in nums:
            for n in list(str(num)):
                digits.append(int(n))

        return digits