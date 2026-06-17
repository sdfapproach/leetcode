# https://leetcode.com/problems/process-string-with-special-operations-ii/?envType=daily-question&envId=2026-06-17
# Process String with Special Operations II

class Solution:
    def processStr(self, s: str, k: int) -> str:
        
        lengths = []
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:
                pass

            lengths.append(length)

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0
            cur_len = lengths[i]

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if k >= prev_len:
                    k -= prev_len

            else:
                k = cur_len - 1 - k

        return '.'