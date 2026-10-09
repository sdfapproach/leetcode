# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/?envType=daily-question&envId=2026-10-09
# Minimum Insertions to Balance a Parentheses String

class Solution:
    def minInsertions(self, s: str) -> int:
        
        answer = 0
        need = 0

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    answer += 1
                    need -= 1

                need += 2

            else:
                need -= 1

                if need < 0:
                    answer += 1
                    need = 1

        return answer + need