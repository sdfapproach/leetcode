# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/?envType=daily-question&envId=2026-06-04
# Total Waviness of Numbers in Range I

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def waviness_sum_upto(N: int) -> int:
            if N < 0:
                return 0
    
            s = str(N)
            n = len(s)
    
            @lru_cache(maxsize=None)
            def dp(pos, prev, pprev, tight, started):
                
                if pos == n:
                    return (1, 0)
    
                limit = int(s[pos]) if tight else 9
                cnt, wav = 0, 0
    
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
    
                    if not started and d == 0:
                        c, w = dp(pos + 1, -1, -1, new_tight, False)
                        cnt += c
                        wav += w
    
                    else:
                        extra = 0
                        if pprev != -1:
                            if (prev > pprev and prev > d) or \
                            (prev < pprev and prev < d):
                                extra = 1
    
                        c, w = dp(pos + 1, d, prev if started else -1, new_tight, True)
                        cnt += c
                        wav += w + extra * c
    
                return (cnt, wav)
    
            _, total = dp(0, -1, -1, True, False)
            return total
    
        return waviness_sum_upto(num2) - waviness_sum_upto(num1 - 1)