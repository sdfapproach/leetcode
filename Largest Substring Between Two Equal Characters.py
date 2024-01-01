# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31
# Largest Substring Between Two Equal Characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # max_len = -1

        # def find_idx(char, string):
        #     idx = -1
        #     for i, c in enumerate(string):
        #         if c == char:
        #             idx = i
        #     return idx

        # for i, c in enumerate(s):
        #     idx = find_idx(c, s[i+1:])

        #     if idx> max_len:
        #         max_len = idx

        # return max_len

        last_occurrence = {}
        max_len = -1

        for i, char in enumerate(s):
            if char in last_occurrence:
                max_len = max(max_len, i - last_occurrence[char] - 1)
            else:
                last_occurrence[char] = i

        return max_len