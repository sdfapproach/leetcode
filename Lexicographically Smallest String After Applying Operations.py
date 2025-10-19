# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/?envType=daily-question&envId=2025-10-19
# Lexicographically Smallest String After Applying Operations

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        n = len(s)
        s_digits = [int(ch) for ch in s]
        ans = s

        a %= 10

        seen_rot = set()
        r = 0
        while r not in seen_rot:
            seen_rot.add(r)
            rot = s_digits[-r:] + s_digits[:-r] if r else s_digits[:]

            for i in range(10):
                add_odd = (i * a) % 10
                if b % 2 == 0:
                    even_range = [0]
                else:
                    even_range = list(range(10))

                for j in even_range:
                    add_even = (j * a) % 10

                    tmp = []
                    for idx, d in enumerate(rot):
                        if idx % 2 == 0:
                            nd = (d + add_even) % 10
                        else:
                            nd = (d + add_odd) % 10
                        tmp.append(str(nd))

                    cand = "".join(tmp)
                    if cand < ans:
                        ans = cand

            r = (r + b) % n

        return ans