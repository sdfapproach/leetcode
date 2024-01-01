# https://leetcode.com/problems/assign-cookies/description/?envType=daily-question&envId=2024-01-01
# Assign Cookies

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # assign = 0

        # g.sort()
        # s.sort()

        # for child in g:
        #     for cookie in s:
        #         if child <= cookie:
        #             s.remove(cookie)
        #             assign += 1
        #             break

        # return assign

        assign = 0

        g.sort()
        s.sort()

        g_index, s_index = 0, 0

        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                assign += 1
                g_index += 1
            s_index += 1

        return assign