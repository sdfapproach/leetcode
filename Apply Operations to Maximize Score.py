# https://leetcode.com/problems/apply-operations-to-maximize-score/?envType=daily-question&envId=2025-03-29
# Apply Operations to Maximize Score

def prime_score(x: int) -> int:
    score = 0
    factor = 2
    while factor * factor <= x:
        if x % factor == 0:
            score += 1
            while x % factor == 0:
                x //= factor
        factor += 1
    if x > 1:
        score += 1
    return score

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        mod = 10**9 + 7
        arr = [(i, prime_score(x), x) for i, x in enumerate(nums)]
        n = len(nums)

        left = [-1] * n
        right = [n] * n
        stk = []
        for i, f, x in arr:
            while stk and stk[-1][0] < f:
                stk.pop()
            if stk:
                left[i] = stk[-1][1]
            stk.append((f, i))

        stk = []
        for i, f, x in arr[::-1]:
            while stk and stk[-1][0] <= f:
                stk.pop()
            if stk:
                right[i] = stk[-1][1]
            stk.append((f, i))

        arr.sort(key=lambda x: -x[2])
        ans = 1
        for i, f, x in arr:
            l, r = left[i], right[i]
            cnt = (i - l) * (r - i)
            if cnt <= k:
                ans = ans * pow(x, cnt, mod) % mod
                k -= cnt
            else:
                ans = ans * pow(x, k, mod) % mod
                break
        return ans