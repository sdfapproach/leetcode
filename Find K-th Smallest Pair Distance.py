# https://leetcode.com/problems/find-k-th-smallest-pair-distance/?envType=daily-question&envId=2024-08-14
# Find K-th Smallest Pair Distance

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def count_pairs(mid):
            count, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        
        return lo