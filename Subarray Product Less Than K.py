# https://leetcode.com/problems/subarray-product-less-than-k/?envType=daily-question&envId=2024-03-27
# Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # count = 0

        # for i in range(len(nums)):

        #     for j in range(len(nums) - i):
        #         product = 1
        #         arr = nums[j:i+1+j]

        #         for n in arr:
        #             product *= n

        #         if product < k:
        #             count += 1

        # return count

        if k <= 1:
            return 0

        prod = 1
        ans = left = 0

        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans