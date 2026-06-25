# https://leetcode.com/problems/count-subarrays-with-majority-element-i/?envType=daily-question&envId=2026-06-25
# Count Subarrays With Majority Element I

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        prefix = 0
        sorted_prefix = [0]
        ans = 0

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bisect_left(sorted_prefix, prefix)

            insort(sorted_prefix, prefix)

        return ans