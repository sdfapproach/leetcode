# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/?envType=daily-question&envId=2024-04-29
# Minimum Number of Operations to Make Array XOR Equal to K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        currentXOR = 0
        for num in nums:
            currentXOR ^= num

        desiredXOR = currentXOR ^ k
        
        flips = 0

        while desiredXOR:
            if desiredXOR & 1:
                flips += 1
            desiredXOR >>= 1

        return flips