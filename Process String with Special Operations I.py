# https://leetcode.com/problems/process-string-with-special-operations-i/?envType=daily-question&envId=2026-06-16
# Process String with Special Operations I

class Solution:
    def processStr(self, s: str) -> str:
        
        result = ""

        for ch in s:
            if 'a' <= ch <= 'z':
                result += ch

            elif ch == '*':
                result = result[:-1]

            elif ch == '#':
                result += result

            else:  # '%'
                result = result[::-1]

        return result