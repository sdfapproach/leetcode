# https://leetcode.com/problems/single-number-iii/?envType=daily-question&envId=2024-05-31
# Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # elements = []
        # counted_nums = Counter(nums)

        # for key, value in counted_nums.items():

        #     if value == 1:
        #         elements.append(key)

        # return elements

        xor = 0
        for num in nums:
            xor ^= num
        
        diff_bit = xor & -xor
        
        x = 0
        y = 0
        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num
        
        return [x, y]