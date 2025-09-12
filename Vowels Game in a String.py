# https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12
# Vowels Game in a String

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = set("aeiouAEIOU")
        
        return any(ch in vowels for ch in s)