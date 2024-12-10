# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/?envType=daily-question&envId=2024-12-10
# Find Longest Special Substring That Occurs Thrice I

class Solution:
    def maximumLength(self, s: str) -> int:
        
        def check(x: int) -> bool:
            cnt = defaultdict(int)
            i = 0
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                cnt[s[i]] += max(0, j - i - x + 1)
                i = j
            return max(cnt.values()) >= 3

        n = len(s)
        l, r = 0, n

        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return -1 if l == 0 else l