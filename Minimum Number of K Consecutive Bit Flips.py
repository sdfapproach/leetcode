# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/?envType=daily-question&envId=2024-06-24
# Minimum Number of K Consecutive Bit Flips

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        n = len(nums)
        is_flipped = [0] * n
        flips = 0
        flip_count = 0

        for i in range(n):
            if i >= k:
                flip_count ^= is_flipped[i - k]
            
            if flip_count % 2 == nums[i]:
                if i + k > n:
                    return -1
                is_flipped[i] = 1
                flip_count ^= 1
                flips += 1

        return flips