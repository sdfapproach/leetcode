# https://leetcode.com/problems/determine-if-string-halves-are-alike/?envType=daily-question&envId=2024-01-12
# Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}

        half = len(s)//2 - 1
        count_a = 0
        count_b = 0

        for i, char in enumerate(s.lower()):
            if i <= half:
                if char in vowels:
                    count_a += 1
            else:
                if char in vowels:
                    count_b += 1

        return count_a == count_b