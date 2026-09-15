# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/?envType=daily-question&envId=2026-09-15
# Maximum Number of Non-overlapping Palindrome Substrings

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)

        dp = [0] * (n + 1)

        for end in range(k, n + 1):
            dp[end] = dp[end - 1]

            start = end - k

            if self.isPalindrome(s, start, end - 1):
                dp[end] = max(
                    dp[end],
                    dp[start] + 1
                )

            if end >= k + 1:
                start = end - k - 1

                if self.isPalindrome(s, start, end - 1):
                    dp[end] = max(
                        dp[end],
                        dp[start] + 1
                    )

        return dp[n]

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True