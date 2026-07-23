# https://leetcode.com/problems/number-of-unique-xor-triplets-i/?envType=daily-question&envId=2026-07-23
# Number of Unique XOR Triplets I

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n <= 2:
            return n

        return 1 << n.bit_length()