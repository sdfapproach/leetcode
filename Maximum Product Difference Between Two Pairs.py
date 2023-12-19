# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/?envType=daily-question&envId=2023-12-18
# Maximum Product Difference Between Two Pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # new_list = sorted(nums)

        # return new_list[-1]*new_list[-2] - new_list[0]*new_list[1]

        max1, max2 = float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')

        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        return max1 * max2 - min1 * min2