# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/?envType=daily-question&envId=2026-04-17
# Minimum Absolute Distance Between Mirror Pairs

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        last_seen = {}
        min_dist = float('inf')

        for j, num in enumerate(nums):
            if num in last_seen:
                min_dist = min(min_dist, j - last_seen[num])

            rev_num = int(str(num)[::-1])
            last_seen[rev_num] = j

        return min_dist if min_dist != float('inf') else -1