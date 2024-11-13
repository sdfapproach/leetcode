# https://leetcode.com/problems/count-the-number-of-fair-pairs/?envType=daily-question&envId=2024-11-13
# Count the Number of Fair Pairs

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        # count = 0

        # for i, num in enumerate(nums):
        #     for j, n in enumerate(nums[i+1:]):

        #         if num + n <= upper and num + n >= lower:
        #             count += 1


        # return count

        nums.sort()
        count = 0
        n = len(nums)

        def count_less_equal(target):
            left, right = 0, n - 1
            pair_count = 0

            while left < right:
                if nums[left] + nums[right] <= target:
                    pair_count += (right - left)
                    left += 1
                else:
                    right -= 1
            return pair_count

        return count_less_equal(upper) - count_less_equal(lower - 1)