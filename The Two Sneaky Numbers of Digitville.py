# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/?envType=daily-question&envId=2025-10-31
# The Two Sneaky Numbers of Digitville

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        sneaky = []
        num_set = set()


        for num in nums:
            if num in num_set:
                sneaky.append(num)
            else:
                num_set.add(num)

        return sneaky
