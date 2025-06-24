# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/?envType=daily-question&envId=2025-06-24
# Find All K-Distant Indices in an Array

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        keys = [i for i, num in enumerate(nums) if num == key]

        k_dist = []

        for i, num in enumerate(nums):
            for key in keys:
                if abs(key-i) <= k:
                    k_dist.append(i)
                    break

        return k_dist