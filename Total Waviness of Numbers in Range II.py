# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/?envType=daily-question&envId=2026-06-05
# Total Waviness of Numbers in Range II

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n):

            if n < 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, prev2, prev1, started, tight):

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wave = dfs(pos + 1, -1, -1, False, ntight)

                        total_cnt += cnt
                        total_wave += wave

                    else:
                        add = 0

                        if prev2 != -1:
                            if ((prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d)):
                                add = 1

                        if prev1 == -1:
                            cnt, wave = dfs(pos + 1, -1, d, True, ntight)

                        else:
                            cnt, wave = dfs(pos + 1, prev1, d, True, ntight)

                        total_cnt += cnt
                        total_wave += wave + add * cnt

                return (total_cnt, total_wave)

            return dfs(0, -1, -1, False, True)[1]

        return solve(num2) - solve(num1 - 1)