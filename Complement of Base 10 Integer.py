# https://leetcode.com/problems/complement-of-base-10-integer/?envType=daily-question&envId=2026-03-11
# Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        return int("".join(['0' if bi == "1" else "1" for bi in bin(n)[2:]]), 2)

        