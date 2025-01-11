# https://leetcode.com/problems/construct-k-palindrome-strings/?envType=daily-question&envId=2025-01-11
# Construct K Palindrome Strings

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False

        char_count = Counter(s)

        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

        return odd_count <= k