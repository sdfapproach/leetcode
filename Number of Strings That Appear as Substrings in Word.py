# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/?envType=daily-question&envId=2026-06-29
# Number of Strings That Appear as Substrings in Word

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        count = 0
        
        for pattern in patterns:
            if pattern in word:
                count += 1

        return count