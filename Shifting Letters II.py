# https://leetcode.com/problems/shifting-letters-ii/?envType=daily-question&envId=2025-01-05
# Shifting Letters II

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        shift = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                shift[end + 1] -= 1
            else:
                shift[start] -= 1
                shift[end + 1] += 1
        
        for i in range(1, n):
            shift[i] += shift[i - 1]

        result = []
        for i in range(n):
            new_char = chr(((ord(s[i]) - ord('a') + shift[i]) % 26) + ord('a'))
            result.append(new_char)

        return ''.join(result)