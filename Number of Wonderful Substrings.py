# https://leetcode.com/problems/number-of-wonderful-substrings/?envType=daily-question&envId=2024-04-30
# Number of Wonderful Substrings

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1
        mask = 0
        total = 0

        for char in word:
            mask ^= (1 << (ord(char) - ord('a')))
            
            total += count[mask]
            
            for i in range(10):
                total += count[mask ^ (1 << i)]
            
            count[mask] += 1

        return total