# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=daily-question&envId=2024-01-14
# Determine if Two Strings Are Close

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # list1 = [n for n in counter1.values()]
        # list2 = [n for n in counter2.values()]

        # char1 = [c for c in counter1.keys()]
        # char2 = [c for c in counter2.keys()]

        # return sorted(list1) == sorted(list2) and sorted(char1) == sorted(char2)

        return sorted(counter1.keys()) == sorted(counter2.keys()) and sorted(counter1.values()) == sorted(counter2.values())