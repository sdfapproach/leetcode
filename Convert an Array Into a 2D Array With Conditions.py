# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2024-01-02
# Convert an Array Into a 2D Array With Conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        new_list = []

        while len(nums) > 0:
            n_list = []

            for n in nums:
                if n not in n_list:
                    n_list.append(n)

            new_list.append(n_list)

            for n in n_list:
                nums.remove(n)

        return new_list