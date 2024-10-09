# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/?envType=daily-question&envId=2024-10-08
# Minimum Number of Swaps to Make the String Balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        
        balance = 0
        max_unbalanced = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
                
            max_unbalanced = min(max_unbalanced, balance)
        
        return (-max_unbalanced + 1) // 2