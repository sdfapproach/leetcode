# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05
# Minimum Length of String After Deleting Similar Ends

class Solution:
    def minimumLength(self, s: str) -> int:

        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            current_char = s[left]
            
            while left <= right and s[left] == current_char:
                left += 1
                
            while left <= right and s[right] == current_char:
                right -= 1

        return max(0, right + 1 - left)