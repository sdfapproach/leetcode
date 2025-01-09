# https://leetcode.com/problems/counting-words-with-a-given-prefix/?envType=daily-question&envId=2025-01-09
# Counting Words With a Given Prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        
        for word in words:

            if pref == word[:len(pref)]:
                count += 1

        return count