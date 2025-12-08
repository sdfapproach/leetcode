# https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08
# Count Square Sum Triples

class Solution:
    def countTriples(self, n: int) -> int:
        
        squares = {i * i for i in range(1, n + 1)}
        
        ans = 0
        
        for a in range(1, n + 1):
            a2 = a * a

            for b in range(1, n + 1):
                s = a2 + b * b
                c = int(s ** 0.5)

                if c * c == s and c <= n:
                    ans += 1
        
        return ans