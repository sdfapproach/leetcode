# https://leetcode.com/problems/gcd-of-odd-and-even-sums/?envType=daily-question&envId=2026-07-15
# GCD of Odd and Even Sums

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        return math.gcd(n**2, n**2+n)