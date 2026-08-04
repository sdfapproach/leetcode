# https://leetcode.com/problems/find-missing-elements/?envType=daily-question&envId=2026-08-04
# Find Missing Elements

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        s = set(nums)

        answer = []

        for x in range(min(nums), max(nums) + 1):
            if x not in s:
                answer.append(x)

        return answer