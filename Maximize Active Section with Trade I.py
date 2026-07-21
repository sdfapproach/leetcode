# https://leetcode.com/problems/maximize-active-section-with-trade-i/?envType=daily-question&envId=2026-07-21
# Maximize Active Section with Trade I

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        initial_ones = s.count('1')

        t = '1' + s + '1'
        zero_blocks = []

        i = 0

        while i < len(t):
            if t[i] == '1':
                i += 1
                continue

            j = i

            while j < len(t) and t[j] == '0':
                j += 1

            zero_blocks.append(j - i)
            i = j

        max_gain = 0

        for i in range(len(zero_blocks) - 1):
            max_gain = max(
                max_gain,
                zero_blocks[i] + zero_blocks[i + 1]
            )

        return initial_ones + max_gain