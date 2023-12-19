# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/?envType=daily-question&envId=2023-12-18
# Maximum Product Difference Between Two Pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        new_list = sorted(nums)

        return new_list[-1]*new_list[-2] - new_list[0]*new_list[1]