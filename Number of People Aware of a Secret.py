# https://leetcode.com/problems/number-of-people-aware-of-a-secret/?envType=daily-question&envId=2025-09-09
# Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        MOD = 10**9 + 7
        new = [0] * (n + 1)
        new[1] = 1

        share = 0
        active = 1

        for d in range(2, n + 1):
            if d - delay >= 1:
                share = (share + new[d - delay]) % MOD
            if d - forget >= 1:
                share = (share - new[d - forget]) % MOD

            new[d] = share % MOD

            active = (active + new[d]) % MOD
            if d - forget >= 1:
                active = (active - new[d - forget]) % MOD

        return active % MOD