# https://leetcode.com/problems/unique-number-of-occurrences/?envType=daily-question&envId=2024-01-17
# Unique Number of Occurrences

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        occurrences = []

        for n in Counter(arr).values():
            if n in occurrences:
                return False
            else:
                occurrences.append(n)

        return True