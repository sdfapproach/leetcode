# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/?envType=daily-question&envId=2025-04-27
# Count Subarrays of Length Three With a Condition

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        count = 0

        for i in range(len(nums)-2):
            sub_arr = nums[i:i+3]

            if sub_arr[0] + sub_arr[2]  == sub_arr[1] / 2:
                count += 1

        return count