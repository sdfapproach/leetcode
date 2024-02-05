# https://leetcode.com/problems/first-unique-character-in-a-string/?envType=daily-question&envId=2024-02-05
# First Unique Character in a String

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count = Counter(s)

        # uniques = [k for k, v in count.items() if v == 1]

        # if len(uniques) < 1:
        #     return -1
        # else:
        #     uniques_idx = []
        #     for char in uniques:
        #         uniques_idx.append(s.index(char))
        #     uniques_idx.sort()

        #     return uniques_idx[0]

        count = Counter(s)

        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx

        return -1