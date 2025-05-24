# https://leetcode.com/problems/find-words-containing-character/?envType=daily-question&envId=2025-05-24
# Find Words Containing Character

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        return [i for i in range(len(words)) if x in words[i]]