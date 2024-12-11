# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/?envType=daily-question&envId=2024-12-11
# Maximum Beauty of an Array After Applying Operation

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        max_beauty = 0
        n = len(nums)
        left = 0

        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            max_beauty = max(max_beauty, right - left + 1)

        return max_beauty