# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/?envType=daily-question&envId=2025-06-10
# Maximum Difference Between Even and Odd Frequency I

class Solution:
    def maxDifference(self, s: str) -> int:

        cnt = [0]*26

        for x in s:
            cnt[ord(x)-ord('a')] += 1
        mn, mx = float("inf"), 0

        for x in cnt:
            if not x:
                continue
            if x%2 == 0:
                mn = min(mn, x)
            else:
                mx = max(mx, x)

        return mx-mn