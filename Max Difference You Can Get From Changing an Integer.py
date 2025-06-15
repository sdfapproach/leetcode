# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/?envType=daily-question&envId=2025-06-15
# Max Difference You Can Get From Changing an Integer

class Solution:
    def maxDiff(self, num: int) -> int:
        
        s = str(num)

        a_list = list(s)
        for ch in a_list:
            if ch != '9':
                dmax = ch
                break
        else:
            dmax = None
        if dmax is not None:
            a_str = ''.join('9' if c == dmax else c for c in a_list)
        else:
            a_str = s

        b_list = list(s)
        if b_list[0] != '1':
            dmin = b_list[0]
            b_str = ''.join('1' if c == dmin else c for c in b_list)
        else:
            dmin = None
            for c in b_list:
                if c > '1':
                    dmin = c
                    break
            if dmin is None:
                b_str = s
            else:
                b_str = ''.join('0' if c == dmin else c for c in b_list)

        return int(a_str) - int(b_str)