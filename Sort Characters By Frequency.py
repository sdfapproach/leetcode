# https://leetcode.com/problems/sort-characters-by-frequency/?envType=daily-question&envId=2024-02-07
# Sort Characters By Frequency

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        char = [key*value for key, value in count.items()]

        char.sort(key=len, reverse=True)

        return "".join(char)