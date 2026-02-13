# https://leetcode.com/problems/longest-balanced-substring-ii/?envType=daily-question&envId=2026-02-13
# Longest Balanced Substring II

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 1

        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                ans = max(ans, run)
                run = 1
        ans = max(ans, run)

        def best_two(x: str, y: str, z: str) -> int:
            best = 0
            diff = 0
            first = {0: -1}
            for i, ch in enumerate(s):
                if ch == z:
                    diff = 0
                    first = {0: i}
                    continue
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    continue

                if diff in first:
                    best = max(best, i - first[diff])
                else:
                    first[diff] = i
            return best

        ans = max(ans, best_two('a', 'b', 'c'))
        ans = max(ans, best_two('a', 'c', 'b'))
        ans = max(ans, best_two('b', 'c', 'a'))

        A = B = C = 0
        first3 = {(0, 0): -1}
        best3 = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                A += 1
            elif ch == 'b':
                B += 1
            else:  # 'c'
                C += 1

            key = (A - B, A - C)
            if key in first3:
                best3 = max(best3, i - first3[key])
            else:
                first3[key] = i

        ans = max(ans, best3)
        return ans