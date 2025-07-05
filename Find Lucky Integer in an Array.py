# https://leetcode.com/problems/find-lucky-integer-in-an-array/?envType=daily-question&envId=2025-07-05
# Find Lucky Integer in an Array

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        nums = [key for key, val in Counter(arr).items() if key == val]

        if len(nums) > 0:
            return max(nums)
        else:
            return -1