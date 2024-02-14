# https://leetcode.com/problems/rearrange-array-elements-by-sign/?envType=daily-question&envId=2024-02-14
# Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        rearranged = []

        for num in nums:
            if num > -1:
                positive.append(num)
            else:
                negative.append(num)

        for i in range(len(positive)):
            rearranged.append(positive[i])
            rearranged.append(negative[i])

        return rearranged