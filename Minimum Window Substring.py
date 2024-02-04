# https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-04
# Minimum Window Substring

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # substrings = []

        # count_t = Counter(t)

        # for i in range(len(s)):
        #     substr = ""
        #     temp_count = count_t.copy()

        #     for j in range(i, len(s)):
        #         if s[j] in temp_count:
        #             temp_count[s[j]] -= 1
        #             if temp_count[s[j]] == 0:
        #                 del temp_count[s[j]]

        #         substr += s[j]

        #         if not temp_count:
        #             substrings.append(substr)
        #             break
        
        # if substrings:
        #     return min(substrings, key=len)
        # else:
        #     return ""

        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        filtered_s = [(i, char) for i, char in enumerate(s) if char in dict_t]

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = filtered_s[l][1]

                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1    

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]