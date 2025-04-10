# https://leetcode.com/problems/count-the-number-of-powerful-integers/?envType=daily-question&envId=2025-04-10
# Count the Number of Powerful Integers

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        for ch in s:
            if int(ch) > limit:
                return 0
                
        m = len(s)
        T = 10 ** m
        s_val = int(s)
        
        if s_val > finish:
            return 0
        
        if start <= s_val:
            P_min = 0
        else:
            diff = start - s_val
            P_min = (diff + T - 1) // T
        P_max = (finish - s_val) // T
        
        if P_max < P_min:
            return 0
        
        countP = self.countAllowed(P_max, limit) - self.countAllowed(P_min - 1, limit)
        return countP

    def countAllowed(self, X: int, limit: int) -> int:
        
        if X < 0:
            return 0
        s = str(X)
        n = len(s)
        
        @lru_cache(maxsize=None)
        def dp(pos: int, tight: bool, started: bool) -> int:
           
            if pos == n:
                return 1
            res = 0
            ub = int(s[pos]) if tight else limit
            ub = min(ub, limit)
            for d in range(0, ub + 1):
                new_tight = tight and (d == int(s[pos]))
                new_started = started or (d != 0)
                res += dp(pos + 1, new_tight, new_started)
            return res
        
        return dp(0, True, False)