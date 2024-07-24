# https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
# Sort the Jumbled Numbers

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        # arr = []
        
        # for i, num in enumerate(nums):

        #     number = ""

        #     for j in str(num):

        #         j = int(j)
        #         number += str(mapping[j])

        #     arr.append([int(number), i])

        
        # arr.sort(key = lambda x : x[0])

        # return [nums[i] for _, i in arr]

        def map_number(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))
        
        mapped_nums = [(map_number(num), i) for i, num in enumerate(nums)]
        
        mapped_nums.sort(key=lambda x: x[0])
        
        return [nums[i] for _, i in mapped_nums]