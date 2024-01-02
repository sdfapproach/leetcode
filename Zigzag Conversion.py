# https://leetcode.com/problems/zigzag-conversion/description/
# Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        char_list = [ [] for i in range(numRows)]

        zig = True
        idx = 0

        for i, char in enumerate(s):
            char_list[idx].append(char)

            if i > 0 and i%(numRows-1) == 0:
                if zig == True:
                    zig = False
                else:
                    zig = True

            if zig == True:
                idx += 1
            else:
                idx -= 1

        return ''.join([''.join(row) for row in char_list])