# https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=daily-question&envId=2025-09-15
# Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count = 0
        broken = list(brokenLetters)
        
        for word in text.split():
            b = False
            for char in broken:
                if char in word:
                    b = True
            if b is False:
                count += 1

        return count