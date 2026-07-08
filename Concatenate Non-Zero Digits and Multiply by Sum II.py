# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/?envType=daily-question&envId=2026-07-08
# Concatenate Non-Zero Digits and Multiply by Sum II

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        pow10 = [1] * (n + 1)
        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        prefix_val = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)

        for i, d in enumerate(digits):
            prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD
            prefix_sum[i + 1] = prefix_sum[i] + d

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                prefix_val[right + 1]
                - prefix_val[left] * pow10[length]
            ) % MOD

            digit_sum = prefix_sum[right + 1] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans