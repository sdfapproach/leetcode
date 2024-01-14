# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/?envType=daily-question&envId=2024-01-13
# Minimum Number of Steps to Make Two Strings Anagram

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # s_count = Counter(s)

        # count = 0

        # for char in t:
        #     if s_count[char] > 0:
        #         s_count[char] -= 1
        #         count += 1

        # return len(s) - count

        s_count = Counter(s)
        t_count = Counter(t)

        return sum((s_count - t_count).values())