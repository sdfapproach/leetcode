# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/?envType=daily-question&envId=2025-10-11
# Maximum Total Damage With Spell Casting

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        cnt = Counter(power)
        vals = sorted(cnt)
        gain = [v * cnt[v] for v in vals]

        n = len(vals)
        dp = [0] * n

        for i, v in enumerate(vals):
            j = bisect.bisect_right(vals, v - 3, 0, i) - 1
            take = gain[i] + (dp[j] if j >= 0 else 0)
            notake = dp[i - 1] if i > 0 else 0
            dp[i] = max(notake, take)

        return dp[-1] if dp else 0