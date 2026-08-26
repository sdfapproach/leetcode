# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/?envType=daily-question&envId=2026-08-26
# Shortest and Lexicographically Smallest Beautiful String

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            while ones == k and left <= right and s[left] == '0':
                left += 1

            if ones == k:
                candidate = s[left:right + 1]

                if (
                    not best
                    or len(candidate) < len(best)
                    or (
                        len(candidate) == len(best)
                        and candidate < best
                    )
                ):
                    best = candidate

        return best