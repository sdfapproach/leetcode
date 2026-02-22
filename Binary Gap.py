# https://leetcode.com/problems/binary-gap/?envType=daily-question&envId=2026-02-22
# Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:
        
        dist = 0
        max_dist = 0
        
        bits = bin(n)[3:]

        for bit in bits:

            if bit == "1":
                max_dist = max(dist + 1, max_dist)
                dist = 0
            else:
                dist += 1


        return max_dist