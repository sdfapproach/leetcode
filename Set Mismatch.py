# https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22
# Set Mismatch

from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # answer = [key for key, fre in Counter(nums).items() if fre > 1]

        # num_list = [n+1 for n in range(len(nums))]

        # for n in num_list:
        #     if n not in nums:
        #         answer.append(n)
        
        # return answer

        counter = Counter(nums)
        duplicate = next(key for key, freq in counter.items() if freq == 2)
        missing = next(n for n in range(1, len(nums) + 1) if n not in counter)

        return [duplicate, missing]