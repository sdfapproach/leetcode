# https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2025-02-20
# Find Unique Binary String

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i][i] == '0':
                answer.append('1')
            else:
                answer.append('0')

        return "".join(answer)