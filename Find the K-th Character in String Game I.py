# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/?envType=daily-question&envId=2025-07-03
# Find the K-th Character in String Game I

class Solution:
    def kthCharacter(self, k: int) -> str:
        
        word = "a"

        while len(word) <= k:

            string = ""

            for c in word:

                string += chr((ord(c) % 122) + 1)

            word += string

        return word[k-1]